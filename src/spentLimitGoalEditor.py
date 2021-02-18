from PySide2.QtWidgets import QWidget, QTableWidgetItem
from src.ui.spentLimitGoalEditor_ui import Ui_spentLimitGoalEditor
from PySide2.QtCore import Qt
from src.dao.project import Project
from src.dao.spentcategory import SpentCategory
from src.dao.spentlimitgoal import SpentLimitGoal


class SpentLimitGoalEditor(QWidget):
    def __init__(self, standard_spent_limit, spent_categories):
        super().__init__()
        self.ui = Ui_spentLimitGoalEditor()
        self.ui.setupUi(self)

        # DAO:
        self.__standard_spent_limit = standard_spent_limit
        self.__spent_categories = spent_categories

        self.check_new_categories()

        # load interface and connects:
        self.load_table()
        self.make_connects()

    def make_connects(self):
        self.ui.tableWidget.cellChanged.connect(self.cell_changed)

    def check_new_categories(self):
        #first, check if any category was excluded:
        for spent_limit in self.__standard_spent_limit:
            if (spent_limit.category not in self.__spent_categories):
                self.__standard_spent_limit.remove(spent_limit) 

        #then, check if a new category was added:
        for category in self.__spent_categories:
            is_in_category = False
            for spent_limit in self.__standard_spent_limit:
                if (category == spent_limit.category):
                    is_in_category = True
                    break
            if (is_in_category == False):
                new_goal = SpentLimitGoal()
                new_goal.set_category(category)
                self.__standard_spent_limit.append(new_goal)

    def load_table(self):
        for spent_limit in self.__standard_spent_limit:
            initial_row_count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(initial_row_count)
            
            #create and insert QTableWidgetItems
            twi_category = QTableWidgetItem()
            twi_category.setData(Qt.DisplayRole, spent_limit.category.name)
            twi_category.setFlags(Qt.ItemIsEnabled) # Disable for edition
            self.ui.tableWidget.setItem(initial_row_count, 0, twi_category)
            twi_amount = QTableWidgetItem()
            twi_amount.setData(Qt.DisplayRole, spent_limit.amount)
            self.ui.tableWidget.setItem(initial_row_count, 1, twi_amount)
    
    def cell_changed(self, row : int, column : int):
        if (column == 1):
            self.__standard_spent_limit[row].set_amount(float(self.ui.tableWidget.item(row, column).data(Qt.DisplayRole)))
