# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spentLimitGoalEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_spentLimitGoalEditor(object):
    def setupUi(self, spentLimitGoalEditor):
        if not spentLimitGoalEditor.objectName():
            spentLimitGoalEditor.setObjectName(u"spentLimitGoalEditor")
        spentLimitGoalEditor.resize(400, 300)
        self.gridLayout = QGridLayout(spentLimitGoalEditor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(spentLimitGoalEditor)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.retranslateUi(spentLimitGoalEditor)

        QMetaObject.connectSlotsByName(spentLimitGoalEditor)
    # setupUi

    def retranslateUi(self, spentLimitGoalEditor):
        spentLimitGoalEditor.setWindowTitle(QCoreApplication.translate("spentLimitGoalEditor", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("spentLimitGoalEditor", u"Categoria", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("spentLimitGoalEditor", u"Meta Teto [R$]", None));
    # retranslateUi

