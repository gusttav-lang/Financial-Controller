# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'idealAssetsEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_idealAssetsEditor(object):
    def setupUi(self, idealAssetsEditor):
        if not idealAssetsEditor.objectName():
            idealAssetsEditor.setObjectName(u"idealAssetsEditor")
        idealAssetsEditor.resize(1124, 781)
        self.verticalLayout_2 = QVBoxLayout(idealAssetsEditor)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter_2 = QSplitter(idealAssetsEditor)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.grouBox = QGroupBox(self.splitter_2)
        self.grouBox.setObjectName(u"grouBox")
        self.verticalLayout = QVBoxLayout(self.grouBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget_today = QTableWidget(self.grouBox)
        if (self.tableWidget_today.columnCount() < 1):
            self.tableWidget_today.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_today.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget_today.setObjectName(u"tableWidget_today")

        self.verticalLayout.addWidget(self.tableWidget_today)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add = QPushButton(self.grouBox)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_delete = QPushButton(self.grouBox)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.grouBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_reserva_atual = QLineEdit(self.grouBox)
        self.lineEdit_reserva_atual.setObjectName(u"lineEdit_reserva_atual")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_reserva_atual)


        self.verticalLayout.addLayout(self.formLayout)

        self.splitter_2.addWidget(self.grouBox)
        self.groupBox = QGroupBox(self.splitter_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableWidget_ideal = QTableWidget(self.groupBox)
        if (self.tableWidget_ideal.rowCount() < 3):
            self.tableWidget_ideal.setRowCount(3)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_ideal.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_ideal.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_ideal.setVerticalHeaderItem(2, __qtablewidgetitem3)
        self.tableWidget_ideal.setObjectName(u"tableWidget_ideal")

        self.verticalLayout_3.addWidget(self.tableWidget_ideal)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_reserva_ideal = QLineEdit(self.groupBox)
        self.lineEdit_reserva_ideal.setObjectName(u"lineEdit_reserva_ideal")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_reserva_ideal)


        self.verticalLayout_3.addLayout(self.formLayout_2)

        self.splitter_2.addWidget(self.groupBox)

        self.verticalLayout_2.addWidget(self.splitter_2)

        self.frame = QFrame(idealAssetsEditor)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter = QSplitter(self.frame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.frame_graph_today = QFrame(self.splitter)
        self.frame_graph_today.setObjectName(u"frame_graph_today")
        self.frame_graph_today.setFrameShape(QFrame.StyledPanel)
        self.frame_graph_today.setFrameShadow(QFrame.Raised)
        self.splitter.addWidget(self.frame_graph_today)
        self.frame_graph_ideal = QFrame(self.splitter)
        self.frame_graph_ideal.setObjectName(u"frame_graph_ideal")
        self.frame_graph_ideal.setFrameShape(QFrame.StyledPanel)
        self.frame_graph_ideal.setFrameShadow(QFrame.Raised)
        self.splitter.addWidget(self.frame_graph_ideal)

        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(idealAssetsEditor)

        QMetaObject.connectSlotsByName(idealAssetsEditor)
    # setupUi

    def retranslateUi(self, idealAssetsEditor):
        idealAssetsEditor.setWindowTitle(QCoreApplication.translate("idealAssetsEditor", u"Aloca\u00e7\u00e3o ideal de ativos", None))
        self.grouBox.setTitle(QCoreApplication.translate("idealAssetsEditor", u"Ativos atuais", None))
        ___qtablewidgetitem = self.tableWidget_today.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("idealAssetsEditor", u"Dia", None));
        self.btn_add.setText(QCoreApplication.translate("idealAssetsEditor", u"Adicionar", None))
        self.btn_delete.setText(QCoreApplication.translate("idealAssetsEditor", u"Deletar", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("idealAssetsEditor", u"Descontar esse valor do montante em renda fixa", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("idealAssetsEditor", u"Valor em reserva de emerg\u00eancia:", None))
        self.groupBox.setTitle(QCoreApplication.translate("idealAssetsEditor", u"Ativos ideais", None))
        ___qtablewidgetitem1 = self.tableWidget_ideal.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("idealAssetsEditor", u"M\u00ednimo [%]", None));
        ___qtablewidgetitem2 = self.tableWidget_ideal.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("idealAssetsEditor", u"Ideal [%]", None));
        ___qtablewidgetitem3 = self.tableWidget_ideal.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("idealAssetsEditor", u"M\u00e1ximo [%]", None));
        self.label_2.setText(QCoreApplication.translate("idealAssetsEditor", u"Valor em reserva de emerg\u00eancia:", None))
    # retranslateUi

