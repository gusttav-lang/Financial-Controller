# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1140, 813)
        self.actionNovo = QAction(MainWindow)
        self.actionNovo.setObjectName(u"actionNovo")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionSalvar = QAction(MainWindow)
        self.actionSalvar.setObjectName(u"actionSalvar")
        self.actionFechar = QAction(MainWindow)
        self.actionFechar.setObjectName(u"actionFechar")
        self.actionSobre = QAction(MainWindow)
        self.actionSobre.setObjectName(u"actionSobre")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sw_central = QStackedWidget(self.centralwidget)
        self.sw_central.setObjectName(u"sw_central")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.sw_central.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.sw_central.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.sw_central)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1140, 21))
        self.menuArquivo = QMenu(self.menubar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        self.menuSobre = QMenu(self.menubar)
        self.menuSobre.setObjectName(u"menuSobre")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dw_esquerdo = QDockWidget(MainWindow)
        self.dw_esquerdo.setObjectName(u"dw_esquerdo")
        self.dw_esquerdo.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tw_esquerdo = QTreeWidget(self.dockWidgetContents)
        self.tw_esquerdo.setObjectName(u"tw_esquerdo")
        self.tw_esquerdo.header().setVisible(False)

        self.gridLayout.addWidget(self.tw_esquerdo, 0, 0, 1, 1)

        self.dw_esquerdo.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dw_esquerdo)

        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())
        self.menuArquivo.addAction(self.actionNovo)
        self.menuArquivo.addAction(self.actionAbrir)
        self.menuArquivo.addAction(self.actionSalvar)
        self.menuArquivo.addAction(self.actionFechar)
        self.menuSobre.addAction(self.actionSobre)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Controlador Financeiro", None))
        self.actionNovo.setText(QCoreApplication.translate("MainWindow", u"Novo", None))
#if QT_CONFIG(tooltip)
        self.actionNovo.setToolTip(QCoreApplication.translate("MainWindow", u"Novo Projeto", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionNovo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(tooltip)
        self.actionAbrir.setToolTip(QCoreApplication.translate("MainWindow", u"Abrir Projeto", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionSalvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
#if QT_CONFIG(tooltip)
        self.actionSalvar.setToolTip(QCoreApplication.translate("MainWindow", u"Salvar Projeto", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSalvar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionFechar.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
#if QT_CONFIG(tooltip)
        self.actionFechar.setToolTip(QCoreApplication.translate("MainWindow", u"Fechar Projeto", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionFechar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionSobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.menuArquivo.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
        self.menuSobre.setTitle(QCoreApplication.translate("MainWindow", u"Ajuda", None))
    # retranslateUi

