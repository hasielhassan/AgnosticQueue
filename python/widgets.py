import os
import sys
import time
import random
import traceback
from PySide import QtCore, QtGui
from ui.job_card_form import Ui_Form as card_form
from ui.queue_dialog_form import Ui_Form as dialog_form


class Card(QtGui.QWidget):

    finish_process = QtCore.Signal(QtGui.QWidget)

    def __init__(self, name, worker):
        super(Card, self).__init__()

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

        QtGui.QMessageBox.information(self, "Reported Error", self.error)

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

class Queue(QtGui.QWidget):

    def __init__(self):
        super(Queue, self).__init__()

        self.ui = dialog_form()
        self.ui.setupUi(self)

        self.cards = []
        self.current = []
        self.completed = []

        self.ui.start_button.clicked.connect(self.start_queue)

    def fill_queue(self, data):

        for item_name, item_worker in data:
            self.create_card(item_name, item_worker)

    def create_card(self, name, worker):

        card = Card(name, worker)
        card.finish_process.connect(self.on_card_finish)

        self.cards.insert(0, card)
        self.ui.scrollAreaWidgetContents.layout().addWidget(card, 0)

    def start_queue(self):
        
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
            QtGui.QMessageBox.information(self, "Finish!", "The queue has been completed!")