from PySide2.QtWidgets import QStyledItemDelegate, QWidget, QStyleOptionViewItem, QDoubleSpinBox
from PySide2.QtCore import Qt, QModelIndex, QAbstractItemModel, QObject
from PySide2.QtGui import QValidator


class DoubleSpinBoxWithNone(QDoubleSpinBox):
    def __init__(self, parent = None):
        super().__init__(parent)

    def validate(self, text : str, pos : int):
        if text == '':
            return QValidator.Acceptable
        else:
            return super().validate(text, pos)

class DoubleDelegate(QStyledItemDelegate): 
    def __init__(self, parent = None):
        super().__init__(parent)
        self.is_text_equals_none = True

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex):
        dsb = DoubleSpinBoxWithNone(parent)
        dsb.setMaximum(999999999)
        dsb.setMinimum(-999999999)  # se trocar aqui vai dar problema no textChanged
        dsb.setDecimals(2)
        dsb.textChanged.connect(self.spinBox_textChanged)
        return dsb

    def setEditorData(self, editor: QWidget, index: QModelIndex):
        value = index.model().data(index,Qt.EditRole)
        if value != None:
            editor.setValue(value)
        else:
            editor.setValue(0)

    def setModelData(self, editor: QWidget, model: QAbstractItemModel, index: QModelIndex):
        if self.is_text_equals_none == False:
            model.setData(index, editor.value(), Qt.EditRole)
        else:
            model.setData(index, None, Qt.EditRole)

    def updateEditorGeometry(self, editor: QWidget, option: QStyleOptionViewItem, index: QModelIndex):
        editor.setGeometry(option.rect)

    def spinBox_textChanged(self, text : str):
        if text == "-999999999,00" and self.is_text_equals_none == True:
            return  # gambiarra: entra aqui quando o usuario limpa o texto e tecla enter
        if text == "":
            self.is_text_equals_none = True
        else:
            self.is_text_equals_none = False
        