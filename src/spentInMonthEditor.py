from PySide2.QtWidgets import QWidget, QTableWidgetItem
from src.ui.spentInMonthEditor_ui import Ui_spentInMonthEditor
from PySide2.QtCore import Qt
from src.dao.project import Project
from src.dao.spentcategory import SpentCategory
from src.dao.spentlimitgoal import SpentLimitGoal


class SpentInMonthEditor(QWidget):
    def __init__(self, month, year, spent_in_month, spent_categories):
        super().__init__()
        self.ui = Ui_spentInMonthEditor()
        self.ui.setupUi(self)

        # DAO:
        self.__month = month
        self.__year = year
        self.__spent_in_month = spent_in_month
        self.__spent_categories = spent_categories

        # load interface and connects:
        self.load_tables()
        self.make_connects()

    def make_connects(self):
        pass

    def load_tables(self):
        pass