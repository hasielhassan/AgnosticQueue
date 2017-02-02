# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'job_card_form.ui'
#
# Created: Thu Feb 02 00:01:31 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(474, 90)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.drag_button = QtGui.QPushButton(Form)
        self.drag_button.setMinimumSize(QtCore.QSize(16, 72))
        self.drag_button.setMaximumSize(QtCore.QSize(16, 16777215))
        self.drag_button.setObjectName("drag_button")
        self.horizontalLayout_2.addWidget(self.drag_button)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon_label = QtGui.QLabel(self.widget)
        self.icon_label.setObjectName("icon_label")
        self.horizontalLayout.addWidget(self.icon_label)
        self.name_label = QtGui.QLabel(self.widget)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout.addWidget(self.name_label)
        spacerItem = QtGui.QSpacerItem(297, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.kill_button = QtGui.QPushButton(self.widget)
        self.kill_button.setMinimumSize(QtCore.QSize(24, 24))
        self.kill_button.setMaximumSize(QtCore.QSize(24, 24))
        self.kill_button.setObjectName("kill_button")
        self.horizontalLayout.addWidget(self.kill_button)
        self.verticalLayout.addWidget(self.widget)
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.drag_button.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.icon_label.setText(QtGui.QApplication.translate("Form", "ICON", None, QtGui.QApplication.UnicodeUTF8))
        self.name_label.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.kill_button.setText(QtGui.QApplication.translate("Form", "X", None, QtGui.QApplication.UnicodeUTF8))

