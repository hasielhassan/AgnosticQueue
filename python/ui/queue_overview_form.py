# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'queue_overview_form.ui'
#
# Created: Sun Apr 09 15:07:29 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(449, 86)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lapsed_time_label = QtGui.QLabel(Form)
        self.lapsed_time_label.setObjectName("lapsed_time_label")
        self.horizontalLayout.addWidget(self.lapsed_time_label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.estimated_time_label = QtGui.QLabel(Form)
        self.estimated_time_label.setObjectName("estimated_time_label")
        self.horizontalLayout.addWidget(self.estimated_time_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.general_progress = QtGui.QProgressBar(Form)
        self.general_progress.setProperty("value", 24)
        self.general_progress.setAlignment(QtCore.Qt.AlignCenter)
        self.general_progress.setObjectName("general_progress")
        self.verticalLayout.addWidget(self.general_progress)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Overall Progress", None, QtGui.QApplication.UnicodeUTF8))
        self.lapsed_time_label.setText(QtGui.QApplication.translate("Form", "Lapsed time: 00:00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.estimated_time_label.setText(QtGui.QApplication.translate("Form", "Estimated time remaining: 00:00:00", None, QtGui.QApplication.UnicodeUTF8))

