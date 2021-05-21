# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spentEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_spentEditor(object):
    def setupUi(self, spentEditor):
        if not spentEditor.objectName():
            spentEditor.setObjectName(u"spentEditor")
        spentEditor.resize(400, 300)
        self.gridLayout = QGridLayout(spentEditor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_new = QPushButton(spentEditor)
        self.btn_new.setObjectName(u"btn_new")

        self.gridLayout.addWidget(self.btn_new, 0, 0, 1, 1)


        self.retranslateUi(spentEditor)

        QMetaObject.connectSlotsByName(spentEditor)
    # setupUi

    def retranslateUi(self, spentEditor):
        spentEditor.setWindowTitle(QCoreApplication.translate("spentEditor", u"Spent Editor", None))
        self.btn_new.setText(QCoreApplication.translate("spentEditor", u"Adicionar novo m\u00eas", None))
    # retranslateUi

