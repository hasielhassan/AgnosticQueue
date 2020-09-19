# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'job_card_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from Qt.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from Qt.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from Qt.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(474, 90)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.drag_button = QPushButton(Form)
        self.drag_button.setObjectName(u"drag_button")
        self.drag_button.setMinimumSize(QSize(16, 72))
        self.drag_button.setMaximumSize(QSize(16, 16777215))

        self.horizontalLayout_2.addWidget(self.drag_button)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_label = QLabel(self.widget)
        self.icon_label.setObjectName(u"icon_label")

        self.horizontalLayout.addWidget(self.icon_label)

        self.name_label = QLabel(self.widget)
        self.name_label.setObjectName(u"name_label")

        self.horizontalLayout.addWidget(self.name_label)

        self.horizontalSpacer = QSpacerItem(297, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.kill_button = QPushButton(self.widget)
        self.kill_button.setObjectName(u"kill_button")
        self.kill_button.setMinimumSize(QSize(24, 24))
        self.kill_button.setMaximumSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.kill_button)


        self.verticalLayout.addWidget(self.widget)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.drag_button.setText(QCoreApplication.translate("Form", u"...", None))
        self.icon_label.setText(QCoreApplication.translate("Form", u"ICON", None))
        self.name_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.kill_button.setText(QCoreApplication.translate("Form", u"X", None))
    # retranslateUi

