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
from src.dao.revenueforecast import RevenueForecast
from src.dao.spent import Spent
from src.dao.spentlimitgoal import SpentLimitGoal
from PySide2.QtGui import QColor, QBrush, QFont


class SpentInMonthEditor(QWidget):
    def __init__(self, spent_in_month: SpentInMonth, spent_categories, project_spent_limit_goal):
        super().__init__()
        self.ui = Ui_spentInMonthEditor()
        self.ui.setupUi(self)

        # DAO:
        self.__spent_in_month = spent_in_month
        self.__spent_categories = spent_categories
        self.__project_spent_limit_goal = project_spent_limit_goal

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

        # create category combobox:
        cbd = CategoryComboBoxItemDelegate(self.__spent_categories, self.ui.tableWidget_fixedSpent)
        self.ui.tableWidget_fixedSpent.setItemDelegateForColumn(3,cbd)

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
            twi_category = QTableWidgetItem()
            if (fixed_spent.category != None): # just fill if has been initialized
                twi_category.setData(Qt.DisplayRole, fixed_spent.category.name)
            self.ui.tableWidget_fixedSpent.setItem(current_row, 3, twi_category)
            current_row += 1
    
    def load_income_table(self):        
        number_of_line = 10
        self.ui.tableWidget_income.setRowCount(number_of_line)
        while (len(self.__spent_in_month.revenue_forecast) < number_of_line):
            new_revenue = RevenueForecast()
            self.__spent_in_month.revenue_forecast.append(new_revenue)
        current_row = 0

        for income in self.__spent_in_month.revenue_forecast:
            twi_what = QTableWidgetItem()
            twi_what.setData(Qt.DisplayRole, income.what)
            self.ui.tableWidget_income.setItem(current_row, 0, twi_what)
            twi_how_much = QTableWidgetItem()
            twi_how_much.setData(Qt.DisplayRole, income.how_much)
            self.ui.tableWidget_income.setItem(current_row, 1, twi_how_much)
            twi_how_day = QTableWidgetItem()
            twi_how_day.setData(Qt.DisplayRole, income.day_in_month)
            self.ui.tableWidget_income.setItem(current_row, 2, twi_how_day)
            current_row += 1

    def load_spent_table(self):
        number_of_line = 50
        self.ui.tableWidget_spent.setRowCount(number_of_line)
        while (len(self.__spent_in_month.spent_list) < number_of_line):
            new_spent = Spent()
            self.__spent_in_month.spent_list.append(new_spent)
        current_row = 0

        # create category combobox:
        cbd = CategoryComboBoxItemDelegate(self.__spent_categories, self.ui.tableWidget_spent)
        self.ui.tableWidget_spent.setItemDelegateForColumn(3,cbd)

        for spent in self.__spent_in_month.spent_list:
            twi_how_day = QTableWidgetItem()
            twi_how_day.setData(Qt.DisplayRole, spent.day_in_month)
            self.ui.tableWidget_spent.setItem(current_row, 0, twi_how_day)
            twi_how_much = QTableWidgetItem()
            twi_how_much.setData(Qt.DisplayRole, spent.how_much)
            self.ui.tableWidget_spent.setItem(current_row, 1, twi_how_much)
            twi_where = QTableWidgetItem()
            twi_where.setData(Qt.DisplayRole, spent.where)
            self.ui.tableWidget_spent.setItem(current_row, 2, twi_where)
            twi_category = QTableWidgetItem()
            if (spent.category != None): # just fill if has been initialized
                twi_category.setData(Qt.DisplayRole, spent.category.name)
            self.ui.tableWidget_spent.setItem(current_row, 3, twi_category)
            current_row += 1

    def load_values_table(self):
        pass

    def load_sum_table(self):
        self.check_new_categories_for_spent_limit()
        for spent_limit in self.__spent_in_month.spent_limit_goal:
            initial_row_count = self.ui.tableWidget_sum.rowCount()
            self.ui.tableWidget_sum.insertRow(initial_row_count)
            
            #create and insert QTableWidgetItems
            twi_category = QTableWidgetItem()
            twi_category.setData(Qt.DisplayRole, spent_limit.category.name)
            twi_category.setFlags(Qt.ItemIsEnabled) # Disable for edition
            self.ui.tableWidget_sum.setItem(initial_row_count, 0, twi_category)
            twi_sum = QTableWidgetItem()
            # twi_sum.setData(Qt.DisplayRole, spent_limit.category.name)
            twi_sum.setFlags(Qt.ItemIsEnabled) # Disable for edition
            self.ui.tableWidget_sum.setItem(initial_row_count, 1, twi_sum)
            twi_goal = QTableWidgetItem()
            bold_font = QFont()
            bold_font.setBold(True)
            twi_goal.setFont(bold_font)
            twi_goal.setData(Qt.DisplayRole, spent_limit.amount)
            self.ui.tableWidget_sum.setItem(initial_row_count, 2, twi_goal)
        self.update_spent_sum()

    def load_new_month(self):
        self.check_new_categories_for_spent_limit() # create SpentLimitGoal objects

        # set the project_limit_goal as default
        for project_spent_limit in self.__project_spent_limit_goal:
            for spent_limit in self.__spent_in_month.spent_limit_goal:
                if (spent_limit.category == project_spent_limit.category):
                    spent_limit.set_amount(project_spent_limit.amount)
                    break
            
        # TODO:perguntar se quer importar gastos fixos, receitas e obrigar a planejar teto de gastos

    def update_spent_sum(self):
        # update all categories sum of spent
        row = 0
        for category in self.__spent_categories:
            sum = 0.0
            for fixed_spent in self.__spent_in_month.fixed_spent:
                if fixed_spent.category == category:
                    sum += fixed_spent.how_much
            for spent in self.__spent_in_month.spent_list:
                if spent.category == category:
                    sum += spent.how_much
            self.ui.tableWidget_sum.item(row, 1).setData(Qt.DisplayRole, sum)
            row += 1
    
    def check_new_categories_for_spent_limit(self):
        #first, check if any category was excluded:
        for spent_limit in self.__spent_in_month.spent_limit_goal:
            if (spent_limit.category not in self.__spent_categories):
                self.__spent_in_month.spent_limit_goal.remove(spent_limit) 

        #then, check if a new category was added:
        for category in self.__spent_categories:
            is_in_category = False
            for spent_limit in self.__spent_in_month.spent_limit_goal:
                if (category == spent_limit.category):
                    is_in_category = True
                    break
            if (is_in_category == False):
                new_goal = SpentLimitGoal()
                new_goal.set_category(category)
                self.__spent_in_month.spent_limit_goal.append(new_goal)

    def fixed_spent_cell_changed(self, row : int, column : int):
        if (column == 0):
            self.__spent_in_month.fixed_spent[row].set_what(self.ui.tableWidget_fixedSpent.item(row, column).data(Qt.DisplayRole))
        if (column == 1):
            self.__spent_in_month.fixed_spent[row].set_how_much(float(self.ui.tableWidget_fixedSpent.item(row, column).data(Qt.DisplayRole)))
            self.update_spent_sum()
        if (column == 2):
            self.__spent_in_month.fixed_spent[row].set_day_in_month(int(self.ui.tableWidget_fixedSpent.item(row, column).data(Qt.DisplayRole)))
        if (column == 3):
            category = SpentCategory.get_category_by_name(self.ui.tableWidget_fixedSpent.item(row, column).data(Qt.DisplayRole), self.__spent_categories)
            self.__spent_in_month.fixed_spent[row].set_category(category)
            self.update_spent_sum()
    
    def income_cell_changed(self, row : int, column : int):
        if (column == 0):
            self.__spent_in_month.revenue_forecast[row].set_what(self.ui.tableWidget_income.item(row, column).data(Qt.DisplayRole))
        if (column == 1):
            self.__spent_in_month.revenue_forecast[row].set_how_much(float(self.ui.tableWidget_income.item(row, column).data(Qt.DisplayRole)))
        if (column == 2):
            self.__spent_in_month.revenue_forecast[row].set_day_in_month(int(self.ui.tableWidget_income.item(row, column).data(Qt.DisplayRole)))
    
    def spent_cell_changed(self, row : int, column : int):
        if (column == 0):
            self.__spent_in_month.spent_list[row].set_day(int(self.ui.tableWidget_spent.item(row, column).data(Qt.DisplayRole)), self.__spent_in_month.month, self.__spent_in_month.year)            
        if (column == 1):
            self.__spent_in_month.spent_list[row].set_how_much(float(self.ui.tableWidget_spent.item(row, column).data(Qt.DisplayRole)))
            self.update_spent_sum()
        if (column == 2):
            self.__spent_in_month.spent_list[row].set_where(self.ui.tableWidget_spent.item(row, column).data(Qt.DisplayRole))
        if (column == 3):
            category = SpentCategory.get_category_by_name(self.ui.tableWidget_spent.item(row, column).data(Qt.DisplayRole), self.__spent_categories)
            self.__spent_in_month.spent_list[row].set_category(category)
            self.update_spent_sum()
    
    def values_cell_changed(self, row : int, column : int):
        pass
    
    def sum_cell_changed(self, row : int, column : int):
        if (column == 1):
            if (float(self.ui.tableWidget_sum.item(row, 1).data(Qt.DisplayRole)) <= float(self.ui.tableWidget_sum.item(row, 2).data(Qt.DisplayRole))):
                font_color = QColor(0, 200, 0)
            else:
                font_color = QColor(255, 0, 0)
            self.ui.tableWidget_sum.item(row, 1).setForeground(QBrush(font_color))         
        if (column == 2):
            self.__spent_in_month.spent_limit_goal[row].set_amount(float(self.ui.tableWidget_sum.item(row, column).data(Qt.DisplayRole)))