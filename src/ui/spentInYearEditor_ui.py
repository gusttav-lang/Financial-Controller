# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spentInYearEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_spentInYearEditor(object):
    def setupUi(self, spentInYearEditor):
        if not spentInYearEditor.objectName():
            spentInYearEditor.setObjectName(u"spentInYearEditor")
        spentInYearEditor.resize(933, 616)
        self.verticalLayout = QVBoxLayout(spentInYearEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_ano = QLabel(spentInYearEditor)
        self.lbl_ano.setObjectName(u"lbl_ano")
        font = QFont()
        font.setPointSize(16)
        self.lbl_ano.setFont(font)
        self.lbl_ano.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_ano)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(spentInYearEditor)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_earnings = QTableWidget(self.groupBox)
        if (self.tableWidget_earnings.columnCount() < 4):
            self.tableWidget_earnings.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_earnings.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_earnings.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_earnings.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_earnings.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_earnings.setObjectName(u"tableWidget_earnings")

        self.gridLayout.addWidget(self.tableWidget_earnings, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lbl_sum_earnings = QLabel(self.groupBox)
        self.lbl_sum_earnings.setObjectName(u"lbl_sum_earnings")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.lbl_sum_earnings.setFont(font1)

        self.horizontalLayout_2.addWidget(self.lbl_sum_earnings)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(spentInYearEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget_spent = QTableWidget(self.groupBox_2)
        if (self.tableWidget_spent.columnCount() < 4):
            self.tableWidget_spent.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_spent.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_spent.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_spent.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_spent.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tableWidget_spent.setObjectName(u"tableWidget_spent")

        self.verticalLayout_2.addWidget(self.tableWidget_spent)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.lbl_sum_spent = QLabel(self.groupBox_2)
        self.lbl_sum_spent.setObjectName(u"lbl_sum_spent")
        self.lbl_sum_spent.setFont(font1)

        self.horizontalLayout_3.addWidget(self.lbl_sum_spent)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.groupBox_3 = QGroupBox(spentInYearEditor)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_chart = QWidget(self.groupBox_3)
        self.widget_chart.setObjectName(u"widget_chart")

        self.gridLayout_2.addWidget(self.widget_chart, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.retranslateUi(spentInYearEditor)

        QMetaObject.connectSlotsByName(spentInYearEditor)
    # setupUi

    def retranslateUi(self, spentInYearEditor):
        spentInYearEditor.setWindowTitle(QCoreApplication.translate("spentInYearEditor", u"Form", None))
        self.lbl_ano.setText(QCoreApplication.translate("spentInYearEditor", u"Ano", None))
        self.groupBox.setTitle(QCoreApplication.translate("spentInYearEditor", u"Previs\u00e3o de recebimentos", None))
        ___qtablewidgetitem = self.tableWidget_earnings.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("spentInYearEditor", u"Onde", None));
        ___qtablewidgetitem1 = self.tableWidget_earnings.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("spentInYearEditor", u"Quanto", None));
        ___qtablewidgetitem2 = self.tableWidget_earnings.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("spentInYearEditor", u"Parcelas", None));
        ___qtablewidgetitem3 = self.tableWidget_earnings.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("spentInYearEditor", u"Total", None));
        self.lbl_sum_earnings.setText(QCoreApplication.translate("spentInYearEditor", u"Soma", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("spentInYearEditor", u"Previs\u00e3o de gastos", None))
        ___qtablewidgetitem4 = self.tableWidget_spent.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("spentInYearEditor", u"Onde", None));
        ___qtablewidgetitem5 = self.tableWidget_spent.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("spentInYearEditor", u"Quanto", None));
        ___qtablewidgetitem6 = self.tableWidget_spent.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("spentInYearEditor", u"Parcelas", None));
        ___qtablewidgetitem7 = self.tableWidget_spent.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("spentInYearEditor", u"Total", None));
        self.lbl_sum_spent.setText(QCoreApplication.translate("spentInYearEditor", u"Soma", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("spentInYearEditor", u"Gastos at\u00e9 o momento", None))
    # retranslateUi

