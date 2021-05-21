from PySide2.QtWidgets import QStyledItemDelegate, QWidget, QStyleOptionViewItem, QSpinBox
from PySide2.QtCore import Qt, QModelIndex, QAbstractItemModel, QObject


class DayInMonthDelegate(QStyledItemDelegate):
    """Creates a QSpinBox delegate for integers between 1 and 31"""
    def __init__(self, parent = None):
        super().__init__(parent)

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex):
        sb = QSpinBox(parent)
        sb.setMaximum(31)
        sb.setMinimum(1) 
        return sb

    def setEditorData(self, editor: QWidget, index: QModelIndex):
        value = index.model().data(index,Qt.EditRole)
        if value != None:
            editor.setValue(value)
        else:
            editor.setValue(0)

    def setModelData(self, editor: QWidget, model: QAbstractItemModel, index: QModelIndex):
        #if self.is_text_equals_none == False:
        model.setData(index, editor.value(), Qt.EditRole)
        #else:
        #    model.setData(index, None, Qt.EditRole)

    def updateEditorGeometry(self, editor: QWidget, option: QStyleOptionViewItem, index: QModelIndex):
        editor.setGeometry(option.rect)