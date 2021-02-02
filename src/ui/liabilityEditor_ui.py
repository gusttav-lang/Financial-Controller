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
        self.horizontalLayout_2 = QHBoxLayout(liabilitiesEditor)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lw_liabilities_list = QListWidget(liabilitiesEditor)
        self.lw_liabilities_list.setObjectName(u"lw_liabilities_list")

        self.verticalLayout.addWidget(self.lw_liabilities_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add = QPushButton(liabilitiesEditor)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_delete = QPushButton(liabilitiesEditor)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(liabilitiesEditor)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_Name = QLineEdit(liabilitiesEditor)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_Name)

        self.label_2 = QLabel(liabilitiesEditor)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.comboBox_brokers = QComboBox(liabilitiesEditor)
        self.comboBox_brokers.setObjectName(u"comboBox_brokers")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_brokers)

        self.label_4 = QLabel(liabilitiesEditor)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.dateEdit_purchase_day = QDateEdit(liabilitiesEditor)
        self.dateEdit_purchase_day.setObjectName(u"dateEdit_purchase_day")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dateEdit_purchase_day)

        self.label_3 = QLabel(liabilitiesEditor)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.dateEdit_expiration_day = QDateEdit(liabilitiesEditor)
        self.dateEdit_expiration_day.setObjectName(u"dateEdit_expiration_day")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dateEdit_expiration_day)

        self.label_5 = QLabel(liabilitiesEditor)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_interest = QLineEdit(liabilitiesEditor)
        self.lineEdit_interest.setObjectName(u"lineEdit_interest")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_interest)

        self.label_6 = QLabel(liabilitiesEditor)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_borrowed_money = QLineEdit(liabilitiesEditor)
        self.lineEdit_borrowed_money.setObjectName(u"lineEdit_borrowed_money")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_borrowed_money)


        self.horizontalLayout_2.addLayout(self.formLayout)


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

