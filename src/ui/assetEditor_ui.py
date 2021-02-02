# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assetEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_assetsEditor(object):
    def setupUi(self, assetsEditor):
        if not assetsEditor.objectName():
            assetsEditor.setObjectName(u"assetsEditor")
        assetsEditor.resize(768, 554)
        self.horizontalLayout_2 = QHBoxLayout(assetsEditor)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lw_assets_list = QListWidget(assetsEditor)
        self.lw_assets_list.setObjectName(u"lw_assets_list")

        self.verticalLayout.addWidget(self.lw_assets_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add = QPushButton(assetsEditor)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_delete = QPushButton(assetsEditor)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(assetsEditor)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_Name = QLineEdit(assetsEditor)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_Name)

        self.label_2 = QLabel(assetsEditor)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(assetsEditor)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(assetsEditor)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.dateEdit_purchase_day = QDateEdit(assetsEditor)
        self.dateEdit_purchase_day.setObjectName(u"dateEdit_purchase_day")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dateEdit_purchase_day)

        self.label_5 = QLabel(assetsEditor)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(assetsEditor)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(assetsEditor)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.dateEdit_expiration_day = QDateEdit(assetsEditor)
        self.dateEdit_expiration_day.setObjectName(u"dateEdit_expiration_day")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dateEdit_expiration_day)

        self.lineEdit_interest = QLineEdit(assetsEditor)
        self.lineEdit_interest.setObjectName(u"lineEdit_interest")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_interest)

        self.lineEdit_applied_money = QLineEdit(assetsEditor)
        self.lineEdit_applied_money.setObjectName(u"lineEdit_applied_money")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_applied_money)

        self.comboBox_objectives = QComboBox(assetsEditor)
        self.comboBox_objectives.setObjectName(u"comboBox_objectives")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.comboBox_objectives)

        self.comboBox_brokers = QComboBox(assetsEditor)
        self.comboBox_brokers.setObjectName(u"comboBox_brokers")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_brokers)


        self.horizontalLayout_2.addLayout(self.formLayout)


        self.retranslateUi(assetsEditor)

        QMetaObject.connectSlotsByName(assetsEditor)
    # setupUi

    def retranslateUi(self, assetsEditor):
        assetsEditor.setWindowTitle(QCoreApplication.translate("assetsEditor", u"Brokers", None))
        self.btn_add.setText(QCoreApplication.translate("assetsEditor", u"Adicionar", None))
        self.btn_delete.setText(QCoreApplication.translate("assetsEditor", u"Deletar", None))
        self.label.setText(QCoreApplication.translate("assetsEditor", u"Nome:", None))
        self.label_2.setText(QCoreApplication.translate("assetsEditor", u"Corretora", None))
        self.label_3.setText(QCoreApplication.translate("assetsEditor", u"Vencimento:", None))
        self.label_4.setText(QCoreApplication.translate("assetsEditor", u"Dia da compra:", None))
        self.label_5.setText(QCoreApplication.translate("assetsEditor", u"Taxa:", None))
        self.label_6.setText(QCoreApplication.translate("assetsEditor", u"Dinheiro aplicado:", None))
        self.label_7.setText(QCoreApplication.translate("assetsEditor", u"Objetivo:", None))
    # retranslateUi

