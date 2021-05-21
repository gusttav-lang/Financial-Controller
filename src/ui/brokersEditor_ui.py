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
        brokersEditor.resize(768, 572)
        self.gridLayout = QGridLayout(brokersEditor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(brokersEditor)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lw_brokers_list = QListWidget(self.widget)
        self.lw_brokers_list.setObjectName(u"lw_brokers_list")

        self.verticalLayout.addWidget(self.lw_brokers_list)

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

        self.lineEdit_bank_number = QLineEdit(self.widget1)
        self.lineEdit_bank_number.setObjectName(u"lineEdit_bank_number")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_bank_number)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.plainTextEdit_description = QPlainTextEdit(self.widget1)
        self.plainTextEdit_description.setObjectName(u"plainTextEdit_description")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.plainTextEdit_description)

        self.splitter.addWidget(self.widget1)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


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

