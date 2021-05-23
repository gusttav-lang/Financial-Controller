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
        spentInMonthEditor.resize(1161, 888)
        self.verticalLayout = QVBoxLayout(spentInMonthEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(spentInMonthEditor)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.splitter_4 = QSplitter(spentInMonthEditor)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.frame_3 = QFrame(self.splitter_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter_3 = QSplitter(self.frame_3)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.splitter_3)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 0, 3, 0)
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

        self.splitter_3.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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

        self.verticalLayout_3.addWidget(self.tableWidget_income)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_sum_earnings = QLabel(self.groupBox_2)
        self.label_sum_earnings.setObjectName(u"label_sum_earnings")
        self.label_sum_earnings.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_sum_earnings)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.splitter_3.addWidget(self.groupBox_2)

        self.horizontalLayout.addWidget(self.splitter_3)

        self.splitter_4.addWidget(self.frame_3)
        self.frame_4 = QFrame(self.splitter_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_4)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.frame_4)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.frame_2 = QFrame(self.splitter_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_2)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(3, 0, 3, 0)
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


        self.gridLayout_8.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.splitter_2.addWidget(self.frame_2)
        self.frame = QFrame(self.splitter_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.frame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.groupBox_4 = QGroupBox(self.splitter)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(3, 0, 3, 0)
        self.tableWidget_values = QTableWidget(self.groupBox_4)
        if (self.tableWidget_values.columnCount() < 1):
            self.tableWidget_values.setColumnCount(1)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_values.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        self.tableWidget_values.setObjectName(u"tableWidget_values")

        self.gridLayout_4.addWidget(self.tableWidget_values, 0, 0, 1, 1)

        self.splitter.addWidget(self.groupBox_4)
        self.groupBox_5 = QGroupBox(self.splitter)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.splitter_5 = QSplitter(self.groupBox_5)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.frame_5 = QFrame(self.splitter_5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget_sum = QTableWidget(self.frame_5)
        if (self.tableWidget_sum.columnCount() < 3):
            self.tableWidget_sum.setColumnCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_sum.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_sum.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_sum.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        self.tableWidget_sum.setObjectName(u"tableWidget_sum")

        self.verticalLayout_2.addWidget(self.tableWidget_sum)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lalbel_sum_spent = QLabel(self.frame_5)
        self.lalbel_sum_spent.setObjectName(u"lalbel_sum_spent")
        self.lalbel_sum_spent.setFont(font1)

        self.horizontalLayout_2.addWidget(self.lalbel_sum_spent)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.splitter_5.addWidget(self.frame_5)
        self.widget_chart = QWidget(self.splitter_5)
        self.widget_chart.setObjectName(u"widget_chart")
        self.splitter_5.addWidget(self.widget_chart)

        self.gridLayout_5.addWidget(self.splitter_5, 0, 0, 1, 1)

        self.splitter.addWidget(self.groupBox_5)

        self.gridLayout_6.addWidget(self.splitter, 0, 0, 1, 1)

        self.splitter_2.addWidget(self.frame)

        self.gridLayout_7.addWidget(self.splitter_2, 0, 0, 1, 1)

        self.splitter_4.addWidget(self.frame_4)

        self.verticalLayout.addWidget(self.splitter_4)


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
        self.label_3.setText(QCoreApplication.translate("spentInMonthEditor", u"Soma:", None))
        self.label_sum_earnings.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("spentInMonthEditor", u"Gatos", None))
        ___qtablewidgetitem7 = self.tableWidget_spent.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("spentInMonthEditor", u"Dia", None));
        ___qtablewidgetitem8 = self.tableWidget_spent.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("spentInMonthEditor", u"Quanto", None));
        ___qtablewidgetitem9 = self.tableWidget_spent.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("spentInMonthEditor", u"Onde", None));
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
        self.label_2.setText(QCoreApplication.translate("spentInMonthEditor", u"Soma:", None))
        self.lalbel_sum_spent.setText("")
    # retranslateUi

