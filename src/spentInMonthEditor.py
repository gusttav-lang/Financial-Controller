from PySide2.QtWidgets import QWidget, QTableWidgetItem
from src.ui.spentInMonthEditor_ui import Ui_spentInMonthEditor
from PySide2.QtCore import Qt
from src.dao.project import Project
from src.dao.spentcategory import SpentCategory
from src.dao.spentlimitgoal import SpentLimitGoal
from src.dao.spentinmonth import SpentInMonth
from src.globalvars import GlobalVars as gv
from src.dao.fixedspent import FixedSpent
from src.tools.CategoryComboBoxItemDelegate import CategoryComboBoxItemDelegate


class SpentInMonthEditor(QWidget):
    def __init__(self, spent_in_month: SpentInMonth, spent_categories):
        super().__init__()
        self.ui = Ui_spentInMonthEditor()
        self.ui.setupUi(self)

        # DAO:
        self.__spent_in_month = spent_in_month
        self.__spent_categories = spent_categories

        if (len(spent_in_month.spent_list) == 0 and len(spent_in_month.fixed_spent) == 0
            and len(spent_in_month.revenue_forecast) == 0):
            self.load_new_month()

        # load interface and connects:
        self.load_tables()
        self.make_connects()

        self.ui.label.setText(gv.Meses[spent_in_month.month] + "/" + str(spent_in_month.year))

    def make_connects(self):        
        self.ui.tableWidget_fixedSpent.cellChanged.connect(self.fixed_spent_cell_changed)
        self.ui.tableWidget_income.cellChanged.connect(self.income_cell_changed)
        self.ui.tableWidget_spent.cellChanged.connect(self.spent_cell_changed)
        self.ui.tableWidget_values.cellChanged.connect(self.values_cell_changed)
        self.ui.tableWidget_sum.cellChanged.connect(self.sum_cell_changed)

    def load_tables(self):
        self.load_fixed_spent_table()
        self.load_income_table()
        self.load_spent_table()
        self.load_values_table()
        self.load_sum_table()        

    def load_fixed_spent_table(self):
        number_of_line = 10
        self.ui.tableWidget_fixedSpent.setRowCount(number_of_line)
        while (len(self.__spent_in_month.fixed_spent) < number_of_line):
            new_fixed_spent = FixedSpent()
            self.__spent_in_month.fixed_spent.append(new_fixed_spent)
        current_row = 0
        for fixed_spent in self.__spent_in_month.fixed_spent:
            twi_what = QTableWidgetItem()
            twi_what.setData(Qt.DisplayRole, fixed_spent.what)
            self.ui.tableWidget_fixedSpent.setItem(current_row, 0, twi_what)
            twi_how_much = QTableWidgetItem()
            twi_how_much.setData(Qt.DisplayRole, fixed_spent.how_much)
            self.ui.tableWidget_fixedSpent.setItem(current_row, 1, twi_how_much)
            twi_how_day = QTableWidgetItem()
            twi_how_day.setData(Qt.DisplayRole, fixed_spent.day_in_month)
            self.ui.tableWidget_fixedSpent.setItem(current_row, 2, twi_how_day)
            #create combobox:
            twi_category = QTableWidgetItem() #nao ta fazendo nado por enquanto
            self.ui.tableWidget_fixedSpent.setItem(current_row, 3, twi_category)
            cbd = CategoryComboBoxItemDelegate(self.__spent_categories, self.ui.tableWidget_fixedSpent)
            self.ui.tableWidget_fixedSpent.setItemDelegateForColumn(3,cbd)

            #twi_how_category = QTableWidgetItem()
            #twi_how_day.setData(Qt.DisplayRole, fixed_spent.day_in_month)
            #self.ui.tableWidget_fixedSpent.setItem(current_row, 2, twi_how_day)
            current_row += 1
    
    def load_income_table(self):
        pass

    def load_spent_table(self):
        pass

    def load_values_table(self):
        pass

    def load_sum_table(self):
        pass

    def load_new_month(self):
        pass # perguntar se quer importar gastos fixos, receitas e obrigar a planejar teto de gastos

    def fixed_spent_cell_changed(self, row : int, column : int):
        if (column == 0):
            self.__spent_in_month.fixed_spent[row].set_what(self.ui.tableWidget_fixedSpent.item(row, column).data(Qt.DisplayRole))
        if (column == 1):
            self.__spent_in_month.fixed_spent[row].set_how_much(float(self.ui.tableWidget_fixedSpent.item(row, column).data(Qt.DisplayRole)))
        if (column == 2):
            self.__spent_in_month.fixed_spent[row].set_day_in_month(int(self.ui.tableWidget_fixedSpent.item(row, column).data(Qt.DisplayRole)))
        if (column == 3):
            self.__spent_in_month.fixed_spent[row].set_category(self.ui.tableWidget_fixedSpent.item(row, column).data(Qt.DisplayRole))
    
    def income_cell_changed(self, row : int, column : int):
        pass
    
    def spent_cell_changed(self, row : int, column : int):
        pass
    
    def values_cell_changed(self, row : int, column : int):
        pass
    
    def sum_cell_changed(self, row : int, column : int):
        pass