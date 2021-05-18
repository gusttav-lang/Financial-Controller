import datetime
from PySide2.QtWidgets import QStyledItemDelegate, QDateEdit, QWidget, QStyleOptionViewItem
from PySide2.QtCore import Qt, QModelIndex, QAbstractItemModel, QRect, QSize, QDate, QObject, QEvent

class DateEditDelegate(QStyledItemDelegate): 
    def __init__(self, parent = None):
        super().__init__(parent)

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex):
        return QDateEdit(parent)

    def setEditorData(self, editor: QWidget, index: QModelIndex):
        #currentDate = datetime.date(index.data(Qt.EditRole))
        if (index.data(Qt.EditRole) != None):
            currentDate = (index.data(Qt.EditRole)).toPython()
            day = currentDate.day
            month = currentDate.month
            year = currentDate.year
            editor.setDate(QDate(year, month, day))

    def setModelData(self, editor: QWidget, model: QAbstractItemModel, index: QModelIndex):
        model.setData(index, editor.date(), Qt.EditRole)

    def updateEditorGeometry(self, editor: QWidget, option: QStyleOptionViewItem, index: QModelIndex):
        editor.setGeometry(option.rect)
        