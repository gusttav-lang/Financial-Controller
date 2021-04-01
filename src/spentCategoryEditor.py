from PySide2.QtWidgets import QWidget, QListWidgetItem
from src.ui.spentCategoryEditor_ui import Ui_spentCategoryEditor
from PySide2.QtCore import Qt
from src.dao.project import Project
from src.dao.spentcategory import SpentCategory


class SpentCategoryEditor(QWidget):
    def __init__(self, spent_categories):
        super().__init__()
        self.ui = Ui_spentCategoryEditor()
        self.ui.setupUi(self)

        # DAO:
        self.__spent_categories = spent_categories

        # load interface and connects:
        self.load_spent_categories()
        self.make_connects()

        # check if can enable delete button
        self.enable_widgets()

        if (self.ui.lw_spent_categories_list.count() > 0):
            self.ui.lw_spent_categories_list.setCurrentRow(-1) # corrects a bug for when there is only 1 item in the list
            self.ui.lw_spent_categories_list.setCurrentRow(0)

    def enable_widgets(self):
        if (self.ui.lw_spent_categories_list.count() == 0):
            self.ui.btn_delete.setEnabled(False)
            self.ui.lineEdit_Name.setEnabled(False)
            self.ui.plainTextEdit_description.setEnabled(False)
        else:            
            self.ui.btn_delete.setEnabled(True)
            self.ui.lineEdit_Name.setEnabled(True)
            self.ui.plainTextEdit_description.setEnabled(True)

    def make_connects(self):
        self.ui.btn_add.clicked.connect(self.add_spent_category)
        self.ui.btn_delete.clicked.connect(self.delete_spent_category)
        self.ui.lw_spent_categories_list.currentRowChanged.connect(self.row_changed)
        self.ui.lineEdit_Name.textChanged.connect(self.name_changed)
        self.ui.lineEdit_Name.textChanged.connect(lambda x: self.__spent_categories[self.ui.lw_spent_categories_list.currentRow()].set_name(x))
        self.ui.plainTextEdit_description.textChanged.connect(self.description_changed)

    def name_changed(self, new_text):
        """Updates de lw_spent_categories ListWidgetItem text"""
        current_row = self.ui.lw_spent_categories_list.currentRow()
        if (current_row > -1 and current_row < self.ui.lw_spent_categories_list.count()):
            self.ui.lw_spent_categories_list.currentItem().setText(new_text)

    def description_changed(self):
        # QPlainTextEdit does not have textChanged(text). We must do it:
        self.__spent_categories[self.ui.lw_spent_categories_list.currentRow()].set_description(self.ui.plainTextEdit_description.toPlainText())
    
    def add_list_widget_item(self, spent_category : SpentCategory):
        item = QListWidgetItem()
        item.setText(spent_category.name)
        self.ui.lw_spent_categories_list.addItem(item)
        self.enable_widgets()        
        self.ui.lw_spent_categories_list.setCurrentRow(self.ui.lw_spent_categories_list.count() - 1)

    def load_spent_categories(self):
        for spent_category in self.__spent_categories:
            self.add_list_widget_item(spent_category)

    def add_spent_category(self):
        # add new spent_category and listwidgetitem
        spent_category = SpentCategory()
        self.__spent_categories.append(spent_category)
        self.add_list_widget_item(spent_category)
        self.enable_widgets()        
        self.ui.lineEdit_Name.selectAll()
        self.ui.lineEdit_Name.setFocus()

    def delete_spent_category(self):
        # delete spent_category
        row = self.ui.lw_spent_categories_list.currentRow()
        if (row > -1 and row < self.ui.lw_spent_categories_list.count()):
            self.ui.lw_spent_categories_list.takeItem(row)
            self.__spent_categories.pop(row)
        self.enable_widgets()

    def row_changed(self, row : int):        
        if (row > -1 and row < self.ui.lw_spent_categories_list.count()):
            self.ui.lineEdit_Name.setText(self.__spent_categories[row].name)
            self.ui.plainTextEdit_description.setPlainText(self.__spent_categories[row].description)
