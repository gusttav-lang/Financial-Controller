# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spentInMonthEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_spentInMonthEditor(object):
    def setupUi(self, spentInMonthEditor):
        if not spentInMonthEditor.objectName():
            spentInMonthEditor.setObjectName(u"spentInMonthEditor")
        spentInMonthEditor.resize(1122, 846)
        self.gridLayout_6 = QGridLayout(spentInMonthEditor)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label = QLabel(spentInMonthEditor)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.gridLayout_6.addWidget(self.label, 0, 1, 1, 1)

        self.groupBox = QGroupBox(spentInMonthEditor)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_fixedSpent = QTableWidget(self.groupBox)
        if (self.tableWidget_fixedSpent.columnCount() < 4):
            self.tableWidget_fixedSpent.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_fixedSpent.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_fixedSpent.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_fixedSpent.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_fixedSpent.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_fixedSpent.setObjectName(u"tableWidget_fixedSpent")

        self.gridLayout.addWidget(self.tableWidget_fixedSpent, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(spentInMonthEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget_income = QTableWidget(self.groupBox_2)
        if (self.tableWidget_income.columnCount() < 3):
            self.tableWidget_income.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_income.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_income.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_income.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tableWidget_income.setObjectName(u"tableWidget_income")

        self.gridLayout_2.addWidget(self.tableWidget_income, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_2, 1, 1, 1, 2)

        self.groupBox_3 = QGroupBox(spentInMonthEditor)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget_spent = QTableWidget(self.groupBox_3)
        if (self.tableWidget_spent.columnCount() < 4):
            self.tableWidget_spent.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_spent.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_spent.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_spent.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_spent.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.tableWidget_spent.setObjectName(u"tableWidget_spent")

        self.gridLayout_3.addWidget(self.tableWidget_spent, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_3, 2, 0, 2, 1)

        self.groupBox_4 = QGroupBox(spentInMonthEditor)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableWidget_values = QTableWidget(self.groupBox_4)
        if (self.tableWidget_values.columnCount() < 1):
            self.tableWidget_values.setColumnCount(1)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_values.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        self.tableWidget_values.setObjectName(u"tableWidget_values")

        self.gridLayout_4.addWidget(self.tableWidget_values, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_4, 2, 1, 1, 2)

        self.groupBox_5 = QGroupBox(spentInMonthEditor)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tableWidget_sum = QTableWidget(self.groupBox_5)
        if (self.tableWidget_sum.columnCount() < 3):
            self.tableWidget_sum.setColumnCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_sum.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_sum.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_sum.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        self.tableWidget_sum.setObjectName(u"tableWidget_sum")

        self.gridLayout_5.addWidget(self.tableWidget_sum, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_5)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_5, 3, 2, 1, 1)


        self.retranslateUi(spentInMonthEditor)

        QMetaObject.connectSlotsByName(spentInMonthEditor)
    # setupUi

    def retranslateUi(self, spentInMonthEditor):
        spentInMonthEditor.setWindowTitle(QCoreApplication.translate("spentInMonthEditor", u"Form", None))
        self.label.setText(QCoreApplication.translate("spentInMonthEditor", u"M\u00eas/Ano", None))
        self.groupBox.setTitle(QCoreApplication.translate("spentInMonthEditor", u"Gastos Fixos", None))
        ___qtablewidgetitem = self.tableWidget_fixedSpent.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("spentInMonthEditor", u"O que", None));
        ___qtablewidgetitem1 = self.tableWidget_fixedSpent.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("spentInMonthEditor", u"Quanto", None));
        ___qtablewidgetitem2 = self.tableWidget_fixedSpent.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("spentInMonthEditor", u"Dia", None));
        ___qtablewidgetitem3 = self.tableWidget_fixedSpent.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("spentInMonthEditor", u"Categoria", None));
        self.groupBox_2.setTitle(QCoreApplication.translate("spentInMonthEditor", u"Previs\u00e3o de receitas", None))
        ___qtablewidgetitem4 = self.tableWidget_income.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("spentInMonthEditor", u"O que", None));
        ___qtablewidgetitem5 = self.tableWidget_income.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("spentInMonthEditor", u"Quanto", None));
        ___qtablewidgetitem6 = self.tableWidget_income.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("spentInMonthEditor", u"Dia", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("spentInMonthEditor", u"Gatos", None))
        ___qtablewidgetitem7 = self.tableWidget_spent.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("spentInMonthEditor", u"O que", None));
        ___qtablewidgetitem8 = self.tableWidget_spent.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("spentInMonthEditor", u"Quanto", None));
        ___qtablewidgetitem9 = self.tableWidget_spent.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("spentInMonthEditor", u"Dia", None));
        ___qtablewidgetitem10 = self.tableWidget_spent.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("spentInMonthEditor", u"Categoria", None));
        self.groupBox_4.setTitle(QCoreApplication.translate("spentInMonthEditor", u"Valorem em conta", None))
        ___qtablewidgetitem11 = self.tableWidget_values.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("spentInMonthEditor", u"Dia verificado", None));
        self.groupBox_5.setTitle(QCoreApplication.translate("spentInMonthEditor", u"Soma final do m\u00eas", None))
        ___qtablewidgetitem12 = self.tableWidget_sum.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("spentInMonthEditor", u"Categoria", None));
        ___qtablewidgetitem13 = self.tableWidget_sum.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("spentInMonthEditor", u"Gasto", None));
        ___qtablewidgetitem14 = self.tableWidget_sum.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("spentInMonthEditor", u"Meta teto m\u00eas", None));
        self.label_2.setText(QCoreApplication.translate("spentInMonthEditor", u"grafico", None))
    # retranslateUi

