# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'liabilityEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_liabilitiesEditor(object):
    def setupUi(self, liabilitiesEditor):
        if not liabilitiesEditor.objectName():
            liabilitiesEditor.setObjectName(u"liabilitiesEditor")
        liabilitiesEditor.resize(768, 554)
        self.gridLayout = QGridLayout(liabilitiesEditor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(liabilitiesEditor)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lw_liabilities_list = QListWidget(self.widget)
        self.lw_liabilities_list.setObjectName(u"lw_liabilities_list")

        self.verticalLayout.addWidget(self.lw_liabilities_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add = QPushButton(self.widget)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_delete = QPushButton(self.widget)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.formLayout = QFormLayout(self.widget1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_Name = QLineEdit(self.widget1)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_Name)

        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.comboBox_brokers = QComboBox(self.widget1)
        self.comboBox_brokers.setObjectName(u"comboBox_brokers")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_brokers)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.dateEdit_purchase_day = QDateEdit(self.widget1)
        self.dateEdit_purchase_day.setObjectName(u"dateEdit_purchase_day")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dateEdit_purchase_day)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.dateEdit_expiration_day = QDateEdit(self.widget1)
        self.dateEdit_expiration_day.setObjectName(u"dateEdit_expiration_day")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dateEdit_expiration_day)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_interest = QLineEdit(self.widget1)
        self.lineEdit_interest.setObjectName(u"lineEdit_interest")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_interest)

        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_borrowed_money = QLineEdit(self.widget1)
        self.lineEdit_borrowed_money.setObjectName(u"lineEdit_borrowed_money")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_borrowed_money)

        self.splitter.addWidget(self.widget1)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(liabilitiesEditor)

        QMetaObject.connectSlotsByName(liabilitiesEditor)
    # setupUi

    def retranslateUi(self, liabilitiesEditor):
        liabilitiesEditor.setWindowTitle(QCoreApplication.translate("liabilitiesEditor", u"Brokers", None))
        self.btn_add.setText(QCoreApplication.translate("liabilitiesEditor", u"Adicionar", None))
        self.btn_delete.setText(QCoreApplication.translate("liabilitiesEditor", u"Deletar", None))
        self.label.setText(QCoreApplication.translate("liabilitiesEditor", u"Nome:", None))
        self.label_2.setText(QCoreApplication.translate("liabilitiesEditor", u"Corretora", None))
        self.label_4.setText(QCoreApplication.translate("liabilitiesEditor", u"Dia da compra:", None))
        self.label_3.setText(QCoreApplication.translate("liabilitiesEditor", u"Vencimento:", None))
        self.label_5.setText(QCoreApplication.translate("liabilitiesEditor", u"Taxa:", None))
        self.label_6.setText(QCoreApplication.translate("liabilitiesEditor", u"Dinheiro emprestado:", None))
    # retranslateUi

