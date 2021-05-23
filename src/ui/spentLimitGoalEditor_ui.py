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
        self.verticalLayout = QVBoxLayout(spentLimitGoalEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(spentLimitGoalEditor)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(spentLimitGoalEditor)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.label_sum = QLabel(spentLimitGoalEditor)
        self.label_sum.setObjectName(u"label_sum")
        self.label_sum.setFont(font)

        self.horizontalLayout.addWidget(self.label_sum)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(spentLimitGoalEditor)

        QMetaObject.connectSlotsByName(spentLimitGoalEditor)
    # setupUi

    def retranslateUi(self, spentLimitGoalEditor):
        spentLimitGoalEditor.setWindowTitle(QCoreApplication.translate("spentLimitGoalEditor", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("spentLimitGoalEditor", u"Categoria", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("spentLimitGoalEditor", u"Meta Teto [R$]", None));
        self.label.setText(QCoreApplication.translate("spentLimitGoalEditor", u"Soma:", None))
        self.label_sum.setText("")
    # retranslateUi

