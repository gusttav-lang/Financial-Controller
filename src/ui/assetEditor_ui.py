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
        self.gridLayout = QGridLayout(assetsEditor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(assetsEditor)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lw_assets_list = QListWidget(self.widget)
        self.lw_assets_list.setObjectName(u"lw_assets_list")

        self.verticalLayout.addWidget(self.lw_assets_list)

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

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.dateEdit_purchase_day = QDateEdit(self.widget1)
        self.dateEdit_purchase_day.setObjectName(u"dateEdit_purchase_day")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dateEdit_purchase_day)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.widget1)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.dateEdit_expiration_day = QDateEdit(self.widget1)
        self.dateEdit_expiration_day.setObjectName(u"dateEdit_expiration_day")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dateEdit_expiration_day)

        self.lineEdit_interest = QLineEdit(self.widget1)
        self.lineEdit_interest.setObjectName(u"lineEdit_interest")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_interest)

        self.lineEdit_applied_money = QLineEdit(self.widget1)
        self.lineEdit_applied_money.setObjectName(u"lineEdit_applied_money")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_applied_money)

        self.comboBox_objectives = QComboBox(self.widget1)
        self.comboBox_objectives.setObjectName(u"comboBox_objectives")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.comboBox_objectives)

        self.comboBox_brokers = QComboBox(self.widget1)
        self.comboBox_brokers.setObjectName(u"comboBox_brokers")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_brokers)

        self.label_8 = QLabel(self.widget1)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_8)

        self.comboBox_categories = QComboBox(self.widget1)
        self.comboBox_categories.setObjectName(u"comboBox_categories")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.comboBox_categories)

        self.label_9 = QLabel(self.widget1)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.plainTextEdit_obs = QPlainTextEdit(self.widget1)
        self.plainTextEdit_obs.setObjectName(u"plainTextEdit_obs")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.plainTextEdit_obs)

        self.splitter.addWidget(self.widget1)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(assetsEditor)

        QMetaObject.connectSlotsByName(assetsEditor)
    # setupUi

    def retranslateUi(self, assetsEditor):
        assetsEditor.setWindowTitle(QCoreApplication.translate("assetsEditor", u"Assets", None))
        self.btn_add.setText(QCoreApplication.translate("assetsEditor", u"Adicionar", None))
        self.btn_delete.setText(QCoreApplication.translate("assetsEditor", u"Deletar", None))
        self.label.setText(QCoreApplication.translate("assetsEditor", u"Nome:", None))
        self.label_2.setText(QCoreApplication.translate("assetsEditor", u"Corretora", None))
        self.label_3.setText(QCoreApplication.translate("assetsEditor", u"Vencimento:", None))
        self.label_4.setText(QCoreApplication.translate("assetsEditor", u"Dia da compra:", None))
        self.label_5.setText(QCoreApplication.translate("assetsEditor", u"Taxa:", None))
        self.label_6.setText(QCoreApplication.translate("assetsEditor", u"Dinheiro aplicado:", None))
        self.label_7.setText(QCoreApplication.translate("assetsEditor", u"Objetivo:", None))
        self.label_8.setText(QCoreApplication.translate("assetsEditor", u"Categoria:", None))
        self.label_9.setText(QCoreApplication.translate("assetsEditor", u"Obeserva\u00e7\u00f5es:", None))
        self.plainTextEdit_obs.setPlaceholderText(QCoreApplication.translate("assetsEditor", u"PlaceHolder escrito no c\u00f3dgo para aceitar quebra de linha", None))
    # retranslateUi

