from PySide2.QtWidgets import QDialog, QMessageBox
from src.ui.addSpentMonth_ui import Ui_addSpentMonth
from PySide2.QtCore import Qt
from src.dao.spentinmonth import SpentInMonth
from datetime import datetime


class AddSpentMonth(QDialog):
    def __init__(self, spent_in_month_list):
        super().__init__()
        self.ui = Ui_addSpentMonth()
        self.ui.setupUi(self)

        # internal vars:
        self.confirmed = False
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month
        self.initial_combobox_year = 2000

        # DAO:
        self.__spent_in_month_list = spent_in_month_list

        # fill year comboBox:
        for i in range(self.initial_combobox_year, self.current_year + 1):
            self.ui.comboBox_year.addItem(str(i))

        self.ui.comboBox_year.setCurrentIndex(self.ui.comboBox_year.count() - 1)
        self.ui.comboBox_month.setCurrentIndex(self.current_month - 1)
        self.selected_year = self.current_year
        self.selected_month = self.current_month

        # connects:
        self.ui.btn_cancel.clicked.connect(lambda x : self.close())
        self.ui.btn_add.clicked.connect(self.add_new_month)
        self.ui.comboBox_year.currentIndexChanged.connect(self.comboBox_year_changed)
        self.ui.comboBox_month.currentIndexChanged.connect(self.comboBox_month_changed)

    def comboBox_year_changed(self, index: int):
        self.selected_year = self.initial_combobox_year + index + 1

    def comboBox_month_changed(self, index : int):
        self.selected_month = index + 1
    
    def add_new_month(self):
        if self.month_already_exists():
            QMessageBox.critical(self, "Erro", "Mês cadastrado já existe!", QMessageBox.Ok)
        else:
            self.confirmed = True
            self.close()

    def month_already_exists(self):
        """Check if the month already exists in spent_in_month_list"""
        for i in self.__spent_in_month_list:
            if (i.year == self.ui.comboBox_year.currentIndex()+1 and i.month == self.ui.comboBox_month.currentIndex() + 1):
                return True
        return False
