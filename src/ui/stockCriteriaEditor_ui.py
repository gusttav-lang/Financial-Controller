# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stockCriteriaEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_stockCriteriaEditor(object):
    def setupUi(self, stockCriteriaEditor):
        if not stockCriteriaEditor.objectName():
            stockCriteriaEditor.setObjectName(u"stockCriteriaEditor")
        stockCriteriaEditor.resize(1151, 865)
        self.verticalLayout = QVBoxLayout(stockCriteriaEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(stockCriteriaEditor)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(stockCriteriaEditor)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.plainTextEdit_indicators = QPlainTextEdit(stockCriteriaEditor)
        self.plainTextEdit_indicators.setObjectName(u"plainTextEdit_indicators")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.plainTextEdit_indicators)

        self.label_2 = QLabel(stockCriteriaEditor)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.plainTextEdit_analysis = QPlainTextEdit(stockCriteriaEditor)
        self.plainTextEdit_analysis.setObjectName(u"plainTextEdit_analysis")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.plainTextEdit_analysis)

        self.label = QLabel(stockCriteriaEditor)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label)

        self.plainTextEdit_valuation = QPlainTextEdit(stockCriteriaEditor)
        self.plainTextEdit_valuation.setObjectName(u"plainTextEdit_valuation")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.plainTextEdit_valuation)

        self.label_5 = QLabel(stockCriteriaEditor)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.plainTextEdit_more_criteria = QPlainTextEdit(stockCriteriaEditor)
        self.plainTextEdit_more_criteria.setObjectName(u"plainTextEdit_more_criteria")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.plainTextEdit_more_criteria)

        self.label_6 = QLabel(stockCriteriaEditor)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.plainTextEdit_number = QPlainTextEdit(stockCriteriaEditor)
        self.plainTextEdit_number.setObjectName(u"plainTextEdit_number")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.plainTextEdit_number)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(stockCriteriaEditor)

        QMetaObject.connectSlotsByName(stockCriteriaEditor)
    # setupUi

    def retranslateUi(self, stockCriteriaEditor):
        stockCriteriaEditor.setWindowTitle(QCoreApplication.translate("stockCriteriaEditor", u"Assets Categories", None))
        self.label_4.setText(QCoreApplication.translate("stockCriteriaEditor", u"Crit\u00e9rios para compra de a\u00e7\u00f5es", None))
        self.label_3.setText(QCoreApplication.translate("stockCriteriaEditor", u"Indicadores:", None))
        self.plainTextEdit_indicators.setPlaceholderText(QCoreApplication.translate("stockCriteriaEditor", u"Escrever quais indicadores vou analisar para comprar uma a\u00e7\u00e3o. Colocar faixar de valores", None))
        self.label_2.setText(QCoreApplication.translate("stockCriteriaEditor", u"An\u00e1lise do investidor:", None))
        self.plainTextEdit_analysis.setPlaceholderText(QCoreApplication.translate("stockCriteriaEditor", u"Escrever o que devo avaliar ao buscar uma empresa. Como ela ganha dinheiro? Quais s\u00e3o os riscos do neg\u00f3cio?", None))
        self.label.setText(QCoreApplication.translate("stockCriteriaEditor", u"Como fazer Valuation:", None))
        self.plainTextEdit_valuation.setPlaceholderText(QCoreApplication.translate("stockCriteriaEditor", u"Descrever passo a passo da metodologia que utilizarei para fazer o valuation", None))
        self.label_5.setText(QCoreApplication.translate("stockCriteriaEditor", u"Demais crit\u00e9rios:", None))
        self.plainTextEdit_more_criteria.setPlaceholderText(QCoreApplication.translate("stockCriteriaEditor", u"Escrever crit\u00e9rios adicionais que eu gostaria de avaliar. Categorias de Lynch? Dimens\u00f5es de Fisher?", None))
        self.label_6.setText(QCoreApplication.translate("stockCriteriaEditor", u"N\u00famero ideal de a\u00e7\u00f5es e setores desejados:", None))
        self.plainTextEdit_number.setPlaceholderText(QCoreApplication.translate("stockCriteriaEditor", u"Escrever n\u00famero m\u00ednimo e m\u00e1ximo de a\u00e7\u00f5es que eu deveria ter. Quais setores da economia eu quero ter? Quantas empresas em cada setor?", None))
    # retranslateUi

