from PySide2.QtWidgets import QTreeWidgetItem, QTreeWidget
from src.dao.yearpredictions import YearPredictions


class TreeWidgetItemYear(QTreeWidgetItem):
    def __init__(self, parent: QTreeWidget, year_predictions: YearPredictions):
        super(TreeWidgetItemYear, self).__init__(parent, type=QTreeWidgetItem.UserType)
        self.year_predictions = year_predictions