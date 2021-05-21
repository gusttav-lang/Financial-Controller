from PySide2.QtWidgets import QTreeWidgetItem, QTreeWidget
from src.dao.spentinmonth import  SpentInMonth

class TreeWidgetItemMonthYear(QTreeWidgetItem):
    def __init__(self, parent: QTreeWidget, spent_in_month: SpentInMonth):
        super(TreeWidgetItemMonthYear, self).__init__(parent, type=QTreeWidgetItem.UserType)
        self.spent_in_month = spent_in_month