
import sys

from Qt import QtCore, QtWidgets
from AgnosticQueue import QueueWidget, CardProcessWorker

class CustomProcessWorker(CardProcessWorker):

    def run(self):

    	#insert your custom process here
        import time
        import random
        for i in range(11):
            time.sleep(random.randint(1,5))
    	    self.updateProgress.emit(i * 10)

#Queue gui
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
queue_app.show()

sys.exit(app.exec_())