# AgnosticQueue
Agnostic Process Queue Template with PySide

Also its a flexible widget tu build a process queue for your own apps.

#Sample:

```python
import sys
from PySide import QtCore, QtGui
import AgnosticQueue as queue

class CustomProcessWorker(queue.widgets.CardProcessWorker):

    def run(self):

    	#insert your custom process here
    	self.updateProgress.emit(100)


#Queue gui
queue_data = []
items = ["one", "two", "tree", "four", "five", "six"]
for item in items:
    worker = CustomProcessWorker(item)
    queue_data.append((item, worker))

app = QtGui.QApplication(sys.argv)

queue_app = Queue()
queue_app.fill_queue(queue_data)
queue_app.resize(450, 150)
queue_app.setWindowTitle('AgnosticQueue')
queue_app.show()

sys.exit(app.exec_())
```