# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'queue_overview_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(449, 86)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lapsed_time_label = QLabel(Form)
        self.lapsed_time_label.setObjectName(u"lapsed_time_label")

        self.horizontalLayout.addWidget(self.lapsed_time_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.estimated_time_label = QLabel(Form)
        self.estimated_time_label.setObjectName(u"estimated_time_label")

        self.horizontalLayout.addWidget(self.estimated_time_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.general_progress = QProgressBar(Form)
        self.general_progress.setObjectName(u"general_progress")
        self.general_progress.setValue(24)
        self.general_progress.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.general_progress)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Overall Progress", None))
        self.lapsed_time_label.setText(QCoreApplication.translate("Form", u"Lapsed time: 00:00:00", None))
        self.estimated_time_label.setText(QCoreApplication.translate("Form", u"Estimated time remaining: 00:00:00", None))
    # retranslateUi

