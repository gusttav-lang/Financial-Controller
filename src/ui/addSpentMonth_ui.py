# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addSpentMonth.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_addSpentMonth(object):
    def setupUi(self, addSpentMonth):
        if not addSpentMonth.objectName():
            addSpentMonth.setObjectName(u"addSpentMonth")
        addSpentMonth.resize(269, 82)
        self.gridLayout_3 = QGridLayout(addSpentMonth)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(addSpentMonth)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(addSpentMonth)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.comboBox_month = QComboBox(addSpentMonth)
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.setObjectName(u"comboBox_month")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_month.sizePolicy().hasHeightForWidth())
        self.comboBox_month.setSizePolicy(sizePolicy)
        self.comboBox_month.setContextMenuPolicy(Qt.NoContextMenu)

        self.gridLayout.addWidget(self.comboBox_month, 0, 1, 1, 1)

        self.comboBox_year = QComboBox(addSpentMonth)
        self.comboBox_year.setObjectName(u"comboBox_year")
        sizePolicy.setHeightForWidth(self.comboBox_year.sizePolicy().hasHeightForWidth())
        self.comboBox_year.setSizePolicy(sizePolicy)
        self.comboBox_year.setContextMenuPolicy(Qt.NoContextMenu)

        self.gridLayout.addWidget(self.comboBox_year, 0, 3, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_add = QPushButton(addSpentMonth)
        self.btn_add.setObjectName(u"btn_add")

        self.gridLayout_2.addWidget(self.btn_add, 0, 0, 1, 1)

        self.btn_cancel = QPushButton(addSpentMonth)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.gridLayout_2.addWidget(self.btn_cancel, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.retranslateUi(addSpentMonth)

        QMetaObject.connectSlotsByName(addSpentMonth)
    # setupUi

    def retranslateUi(self, addSpentMonth):
        addSpentMonth.setWindowTitle(QCoreApplication.translate("addSpentMonth", u"Adicionar novo m\u00eas de gastos", None))
        self.label.setText(QCoreApplication.translate("addSpentMonth", u"M\u00eas:", None))
        self.label_2.setText(QCoreApplication.translate("addSpentMonth", u"Ano:", None))
        self.comboBox_month.setItemText(0, QCoreApplication.translate("addSpentMonth", u"Janeiro", None))
        self.comboBox_month.setItemText(1, QCoreApplication.translate("addSpentMonth", u"Fevereiro", None))
        self.comboBox_month.setItemText(2, QCoreApplication.translate("addSpentMonth", u"Mar\u00e7o", None))
        self.comboBox_month.setItemText(3, QCoreApplication.translate("addSpentMonth", u"Abril", None))
        self.comboBox_month.setItemText(4, QCoreApplication.translate("addSpentMonth", u"Maio", None))
        self.comboBox_month.setItemText(5, QCoreApplication.translate("addSpentMonth", u"Junho", None))
        self.comboBox_month.setItemText(6, QCoreApplication.translate("addSpentMonth", u"Agosto", None))
        self.comboBox_month.setItemText(7, QCoreApplication.translate("addSpentMonth", u"Setembro", None))
        self.comboBox_month.setItemText(8, QCoreApplication.translate("addSpentMonth", u"Outubro", None))
        self.comboBox_month.setItemText(9, QCoreApplication.translate("addSpentMonth", u"Novembro", None))
        self.comboBox_month.setItemText(10, QCoreApplication.translate("addSpentMonth", u"Dezembro", None))

        self.btn_add.setText(QCoreApplication.translate("addSpentMonth", u"Adicionar", None))
        self.btn_cancel.setText(QCoreApplication.translate("addSpentMonth", u"Cancelar", None))
    # retranslateUi

