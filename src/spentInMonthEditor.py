from PySide2.QtWidgets import QWidget, QTableWidgetItem
from src.ui.spentInMonthEditor_ui import Ui_spentInMonthEditor
from PySide2.QtCore import Qt
from src.dao.project import Project
from src.dao.spentcategory import SpentCategory
from src.dao.spentlimitgoal import SpentLimitGoal
from src.dao.spentinmonth import SpentInMonth
from src.globalvars import GlobalVars as gv


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
        pass

    def load_new_month(self):
        pass # perguntar se quer importar gastos fixos, receitas e obrigar a planejar teto de gastos

    def fixed_spent_cell_changed(self, row : int, column : int):
        pass
    
    def income_cell_changed(self, row : int, column : int):
        pass
    
    def spent_cell_changed(self, row : int, column : int):
        pass
    
    def values_spent_cell_changed(self, row : int, column : int):
        pass
    
    def sum_spent_cell_changed(self, row : int, column : int):
        pass