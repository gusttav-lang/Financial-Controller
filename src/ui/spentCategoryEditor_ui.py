# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spentCategoryEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_spentCategoryEditor(object):
    def setupUi(self, spentCategoryEditor):
        if not spentCategoryEditor.objectName():
            spentCategoryEditor.setObjectName(u"spentCategoryEditor")
        spentCategoryEditor.resize(768, 554)
        self.horizontalLayout_2 = QHBoxLayout(spentCategoryEditor)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lw_spent_categories_list = QListWidget(spentCategoryEditor)
        self.lw_spent_categories_list.setObjectName(u"lw_spent_categories_list")

        self.verticalLayout.addWidget(self.lw_spent_categories_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add = QPushButton(spentCategoryEditor)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_delete = QPushButton(spentCategoryEditor)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(spentCategoryEditor)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_Name = QLineEdit(spentCategoryEditor)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_Name)

        self.label_3 = QLabel(spentCategoryEditor)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.plainTextEdit_description = QPlainTextEdit(spentCategoryEditor)
        self.plainTextEdit_description.setObjectName(u"plainTextEdit_description")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.plainTextEdit_description)


        self.horizontalLayout_2.addLayout(self.formLayout)


        self.retranslateUi(spentCategoryEditor)

        QMetaObject.connectSlotsByName(spentCategoryEditor)
    # setupUi

    def retranslateUi(self, spentCategoryEditor):
        spentCategoryEditor.setWindowTitle(QCoreApplication.translate("spentCategoryEditor", u"Brokers", None))
        self.btn_add.setText(QCoreApplication.translate("spentCategoryEditor", u"Adicionar", None))
        self.btn_delete.setText(QCoreApplication.translate("spentCategoryEditor", u"Deletar", None))
        self.label.setText(QCoreApplication.translate("spentCategoryEditor", u"Nome:", None))
        self.label_3.setText(QCoreApplication.translate("spentCategoryEditor", u"Descri\u00e7\u00e3o:", None))
    # retranslateUi

