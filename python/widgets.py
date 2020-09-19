import os
import sys
import time
import random
import pprint
import datetime
import traceback

from Qt import QtCore, QtWidgets

from ui.job_card_form import Ui_Form as card_form
from ui.queue_dialog_form import Ui_Form as dialog_form
from ui.queue_overview_form import Ui_Form as overview_form

class JobCard(QtWidgets.QWidget):

    update_overview = QtCore.Signal(QtWidgets.QWidget, float)
    finish_process = QtCore.Signal(QtWidgets.QWidget)

    def __init__(self, name, worker):
        super(JobCard, self).__init__()

        self.ui = card_form()
        self.ui.setupUi(self)

        self.name = name
        self.ui.name_label.setText(name)

        self.ui.progressBar.setValue(0)

        self.worker = worker
        self.worker.updateProgress.connect(self.setProgress)
        self.worker.failCard.connect(self.setFailedCard)

        self.ui.kill_button.setEnabled(False)
        self.ui.kill_button.clicked.connect(self.show_error)

    def start(self):

        self.worker.start()

    def setProgress(self, value):

        self.update_overview.emit(self, value)

        if value < 100:
            self.ui.progressBar.setValue(value)
        else:
            self.ui.progressBar.setValue(value)
            self.finish_process.emit(self)

    def setFailedCard(self, error):

        self.ui.progressBar.setValue(100)
        self.change_color("Red")

        self.error = error
        self.ui.kill_button.setEnabled(True)
        self.finish_process.emit(self)

    def show_error(self):

        QtWidgets.QMessageBox.information(self, "Reported Error", self.error)

    def change_color(self, color):
        template_css = """QProgressBar::chunk { background: %s; }"""
        css = template_css % color
        self.ui.progressBar.setStyleSheet(css)

class CardProcessWorker(QtCore.QThread):

    updateProgress = QtCore.Signal(float)

    failCard = QtCore.Signal(str)

    def __init__(self, data):
        QtCore.QThread.__init__(self)
        self.data = data

    def run(self):

        seed = random.uniform(0.1,0.8)

        for i in range(1, 101):
            time.sleep(seed)
            self.updateProgress.emit(float(i))

class QueueWidget(QtWidgets.QWidget):

    def __init__(self):
        super(QueueWidget, self).__init__()

        self.cards_progress = {}

        self.ui = dialog_form()
        self.ui.setupUi(self)

        self.setup_overview()

        self.cards = []
        self.current = []
        self.completed = []

        self.ui.start_button.clicked.connect(self.start_queue)

    def setup_overview(self):

        self.overview_widget = QtWidgets.QWidget()
        self.overview_widget.ui = overview_form()
        self.overview_widget.ui.setupUi(self.overview_widget)
        self.overview_widget.ui.general_progress.setValue(0)
        self.ui.verticalLayout.addWidget(self.overview_widget, 0)

    def fill_queue(self, data):

        for item_name, item_worker in data:
            self.create_card(item_name, item_worker)

    def create_card(self, name, worker):

        card = JobCard(name, worker)
        card.finish_process.connect(self.on_card_finish)
        card.update_overview.connect(self.setProgress)

        self.cards.insert(0, card)
        self.ui.scrollAreaWidgetContents.layout().addWidget(card, 0)

    def setProgress(self, card, value):

        self.cards_progress[card.name] = value

        total_cards = sum([len(self.cards), len(self.current), len(self.completed)])
        processed_card_progress = sum([self.cards_progress[item] for item in self.cards_progress])
        overview_value = processed_card_progress / total_cards

        self.overview_widget.ui.general_progress.setValue(overview_value)

        current_time = datetime.datetime.now()
        lapsed_time = current_time - self.start_time

        l_hours = str(lapsed_time.seconds / 3600)
        seconds_left = lapsed_time.seconds % 3600
        l_minutes = str(seconds_left / 60)
        l_seconds = str(seconds_left & 60)
        remaining_string = "Lapsed time:: %s:%s:%s" % (l_hours.zfill(2), l_minutes.zfill(2), l_seconds.zfill(2))
        self.overview_widget.ui.lapsed_time_label.setText(remaining_string)

        if int(overview_value) != 0:
            
            time_remaining = (lapsed_time / int(overview_value)) * (100 - int(overview_value))
            r_hours = str(time_remaining.seconds / 3600)
            seconds_left = time_remaining.seconds % 3600
            r_minutes = str(seconds_left / 60)
            r_seconds = str(seconds_left & 60)
            remaining_string = "Estimated time remaining: %s:%s:%s" % (r_hours.zfill(2), r_minutes.zfill(2), r_seconds.zfill(2))
            self.overview_widget.ui.estimated_time_label.setText(remaining_string)

    def start_queue(self):
        
        self.start_time = datetime.datetime.now()
        self.processes_queue()

    def processes_queue(self):

        while len(self.current) < 3 and len(self.cards) != 0:

            card = self.cards.pop()
            card.start()
            self.current.append(card)

    def on_card_finish(self, card):

        self.current.remove(card)
        self.completed.append(card)

        if len(self.cards) != 0:
            self.processes_queue()
        elif len(self.current) == 0:
            QtWidgets.QMessageBox.information(self, "Finish!", "The queue has been completed!")