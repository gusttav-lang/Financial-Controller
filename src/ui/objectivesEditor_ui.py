# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'objectivesEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_objectivesEditor(object):
    def setupUi(self, objectivesEditor):
        if not objectivesEditor.objectName():
            objectivesEditor.setObjectName(u"objectivesEditor")
        objectivesEditor.resize(768, 554)
        self.horizontalLayout_2 = QHBoxLayout(objectivesEditor)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lw_objectives_list = QListWidget(objectivesEditor)
        self.lw_objectives_list.setObjectName(u"lw_objectives_list")

        self.verticalLayout.addWidget(self.lw_objectives_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add = QPushButton(objectivesEditor)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_delete = QPushButton(objectivesEditor)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(objectivesEditor)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_Name = QLineEdit(objectivesEditor)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_Name)

        self.label_2 = QLabel(objectivesEditor)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_finished_definition = QLineEdit(objectivesEditor)
        self.lineEdit_finished_definition.setObjectName(u"lineEdit_finished_definition")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_finished_definition)

        self.label_3 = QLabel(objectivesEditor)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.plainTextEdit_description = QPlainTextEdit(objectivesEditor)
        self.plainTextEdit_description.setObjectName(u"plainTextEdit_description")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.plainTextEdit_description)

        self.label_4 = QLabel(objectivesEditor)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.dateEdit_deadline = QDateEdit(objectivesEditor)
        self.dateEdit_deadline.setObjectName(u"dateEdit_deadline")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dateEdit_deadline)


        self.horizontalLayout_2.addLayout(self.formLayout)


        self.retranslateUi(objectivesEditor)

        QMetaObject.connectSlotsByName(objectivesEditor)
    # setupUi

    def retranslateUi(self, objectivesEditor):
        objectivesEditor.setWindowTitle(QCoreApplication.translate("objectivesEditor", u"Brokers", None))
        self.btn_add.setText(QCoreApplication.translate("objectivesEditor", u"Adicionar", None))
        self.btn_delete.setText(QCoreApplication.translate("objectivesEditor", u"Deletar", None))
        self.label.setText(QCoreApplication.translate("objectivesEditor", u"Nome:", None))
        self.label_2.setText(QCoreApplication.translate("objectivesEditor", u"Defini\u00e7\u00e3o de conclu\u00eddo:", None))
        self.label_3.setText(QCoreApplication.translate("objectivesEditor", u"Descri\u00e7\u00e3o:", None))
        self.label_4.setText(QCoreApplication.translate("objectivesEditor", u"Deadline:", None))
    # retranslateUi

