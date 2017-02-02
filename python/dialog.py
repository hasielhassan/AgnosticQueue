import os
import sys
import time
import random
from PySide import QtCore, QtGui
from ui.job_card_form import Ui_Form


class Card(QtGui.QWidget):

    finish_process = QtCore.Signal(QtGui.QWidget)

    def __init__(self, name):
        super(Card, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.name = name
        self.ui.name_label.setText(name)

        self.ui.progressBar.setValue(0)

        self.worker = CardProcessWorker()
        self.worker.updateProgress.connect(self.setProgress)

    def start(self):

        self.worker.start()

    def setProgress(self, value):

        if value < 100:
            self.ui.progressBar.setValue(value)
        else:
            self.ui.progressBar.setValue(value)
            self.finish_process.emit(self)

class CardProcessWorker(QtCore.QThread):

    updateProgress = QtCore.Signal(int)

    def __init__(self):
        QtCore.QThread.__init__(self)

        self.seed = random.uniform(0.1,0.8)

    def run(self):
        for i in range(1, 101):
            time.sleep(self.seed)
            self.updateProgress.emit(i)

class Queue(QtGui.QWidget):

    def __init__(self):
        super(Queue, self).__init__()

        self.widget = QtGui.QWidget()
        layout = QtGui.QVBoxLayout(self.widget)

        self.setLayout(layout)

        self.cards = []
        self.current = []
        self.completed = []

        self.start_button = QtGui.QPushButton()
        self.start_button.setText("Start Queue")
        self.start_button.clicked.connect(self.start_queue)
        self.layout().addWidget(self.start_button, 0)

    def fill_queue(self, data):

        for item in data:
            self.create_card(item)

    def create_card(self, name):

        card = Card(name)
        card.finish_process.connect(self.on_card_finish)

        self.cards.insert(0, card)
        self.layout().addWidget(card, 0)

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


app = QtGui.QApplication(sys.argv)

queue_app = Queue()
queue_app.fill_queue(["one", "two", "tree", "four", "five", "six"])
queue_app.resize(450, 150)
queue_app.setWindowTitle('AgnosticQueue')
print os.path.abspath(__file__)
resources_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources')
icon_path = os.path.join(resources_folder, 'queue_icon.png')
print icon_path
queue_app.setWindowIcon(QtGui.QIcon(icon_path))
queue_app.show()

sys.exit(app.exec_())