# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'brokersEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_brokersEditor(object):
    def setupUi(self, brokersEditor):
        if not brokersEditor.objectName():
            brokersEditor.setObjectName(u"brokersEditor")
        brokersEditor.resize(768, 554)
        self.horizontalLayout_2 = QHBoxLayout(brokersEditor)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lw_brokers_list = QListWidget(brokersEditor)
        self.lw_brokers_list.setObjectName(u"lw_brokers_list")

        self.verticalLayout.addWidget(self.lw_brokers_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add = QPushButton(brokersEditor)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_delete = QPushButton(brokersEditor)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(brokersEditor)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_Name = QLineEdit(brokersEditor)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_Name)

        self.label_2 = QLabel(brokersEditor)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_bank_number = QLineEdit(brokersEditor)
        self.lineEdit_bank_number.setObjectName(u"lineEdit_bank_number")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_bank_number)

        self.label_3 = QLabel(brokersEditor)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.plainTextEdit_description = QPlainTextEdit(brokersEditor)
        self.plainTextEdit_description.setObjectName(u"plainTextEdit_description")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.plainTextEdit_description)


        self.horizontalLayout_2.addLayout(self.formLayout)


        self.retranslateUi(brokersEditor)

        QMetaObject.connectSlotsByName(brokersEditor)
    # setupUi

    def retranslateUi(self, brokersEditor):
        brokersEditor.setWindowTitle(QCoreApplication.translate("brokersEditor", u"Brokers", None))
        self.btn_add.setText(QCoreApplication.translate("brokersEditor", u"Adicionar", None))
        self.btn_delete.setText(QCoreApplication.translate("brokersEditor", u"Deletar", None))
        self.label.setText(QCoreApplication.translate("brokersEditor", u"Nome:", None))
        self.label_2.setText(QCoreApplication.translate("brokersEditor", u"N\u00ba Banco", None))
        self.label_3.setText(QCoreApplication.translate("brokersEditor", u"Descri\u00e7\u00e3o:", None))
    # retranslateUi

