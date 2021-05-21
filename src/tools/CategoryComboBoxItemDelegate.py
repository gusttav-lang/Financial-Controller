from PySide2.QtWidgets import QStyledItemDelegate, QComboBox, QWidget, QStyleOptionViewItem
from PySide2.QtCore import Qt, QModelIndex, QAbstractItemModel, QRect, QSize

class CategoryComboBoxItemDelegate(QStyledItemDelegate): 
    def __init__(self, spent_category_list, parent = None):
        super().__init__(parent)
        self.__spent_category_list = spent_category_list

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex):
        cb = QComboBox(parent)
        for spent_category in self.__spent_category_list:
            cb.addItem(spent_category.name)
        return cb

    def setEditorData(self, editor: QWidget, index: QModelIndex):
        currentText = str(index.data(Qt.EditRole))
        cbIndex = editor.findText(currentText)
        if (cbIndex >= 0):
            editor.setCurrentIndex(cbIndex)

    def setModelData(self, editor: QWidget, model: QAbstractItemModel, index: QModelIndex):
        model.setData(index, editor.currentText(), Qt.EditRole)

    def updateEditorGeometry(self, editor: QWidget, option: QStyleOptionViewItem, index: QModelIndex):
        editor.setGeometry(option.rect)