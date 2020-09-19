import os
import sys
import time
import random
from Qt import QtGui, QtWidgets


from python.widgets import *
# you might want to replace previous import with:
#from AgnosticQueue import QueueWidget, CardProcessWorker

class CustomProcessWorker(CardProcessWorker):

    def run(self):

        print self.data

        seed = random.uniform(0.1,0.8)

        for i in range(1, 101):
            time.sleep(seed)
            self.updateProgress.emit(i)

queue_data = []
items = ["one", "two", "tree", "four", "five", "six"]
for item in items:
    worker = CustomProcessWorker(item)
    queue_data.append((item, worker))

app = QtWidgets.QApplication(sys.argv)

queue_app = QueueWidget()
queue_app.fill_queue(queue_data)
queue_app.resize(450, 150)
queue_app.setWindowTitle('AgnosticQueue')

# pretty icon for the qapp :P
resources_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
icon_path = os.path.join(resources_folder, 'queue_icon.png')

queue_app.setWindowIcon(QtGui.QIcon(icon_path))
queue_app.show()

sys.exit(app.exec_())