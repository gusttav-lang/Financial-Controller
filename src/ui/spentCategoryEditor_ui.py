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
        self.gridLayout = QGridLayout(spentCategoryEditor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(spentCategoryEditor)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lw_spent_categories_list = QListWidget(self.widget)
        self.lw_spent_categories_list.setObjectName(u"lw_spent_categories_list")

        self.verticalLayout.addWidget(self.lw_spent_categories_list)

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

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.plainTextEdit_description = QPlainTextEdit(self.widget1)
        self.plainTextEdit_description.setObjectName(u"plainTextEdit_description")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.plainTextEdit_description)

        self.splitter.addWidget(self.widget1)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


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

