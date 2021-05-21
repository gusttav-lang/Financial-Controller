from PySide2.QtWidgets import QWidget, QListWidgetItem
from src.ui.assetCategoryEditor_ui import Ui_assetCategoryEditor
from PySide2.QtCore import Qt
from src.dao.project import Project
from src.dao.assetcategory import AssetCategory


class AssetCategoryEditor(QWidget):
    def __init__(self, asset_categories):
        super().__init__()
        self.ui = Ui_assetCategoryEditor()
        self.ui.setupUi(self)

        # DAO:
        self.__asset_categories = asset_categories

        # load interface and connects:
        self.load_asset_categories()
        self.make_connects()

        # check if can enable delete button
        self.enable_widgets()

        if (self.ui.lw_asset_categories_list.count() > 0):
            self.ui.lw_asset_categories_list.setCurrentRow(-1) # corrects a bug for when there is only 1 item in the list
            self.ui.lw_asset_categories_list.setCurrentRow(0)

    def enable_widgets(self):
        if (self.ui.lw_asset_categories_list.count() == 0):
            self.ui.btn_delete.setEnabled(False)
            self.ui.lineEdit_Name.setEnabled(False)
            self.ui.plainTextEdit_description.setEnabled(False)
            self.ui.plainTextEdit_opportunities.setEnabled(False)
        else:            
            self.ui.btn_delete.setEnabled(True)
            self.ui.lineEdit_Name.setEnabled(True)
            self.ui.plainTextEdit_description.setEnabled(True)
            self.ui.plainTextEdit_opportunities.setEnabled(True)

    def make_connects(self):
        self.ui.btn_add.clicked.connect(self.add_asset_category)
        self.ui.btn_delete.clicked.connect(self.delete_asset_category)
        self.ui.lw_asset_categories_list.currentRowChanged.connect(self.row_changed)
        self.ui.lineEdit_Name.textChanged.connect(self.name_changed)
        self.ui.lineEdit_Name.textChanged.connect(lambda x: self.__asset_categories[self.ui.lw_asset_categories_list.currentRow()].set_name(x))
        self.ui.plainTextEdit_description.textChanged.connect(self.description_changed)
        self.ui.plainTextEdit_opportunities.textChanged.connect(self.opportunity_changed)

    def name_changed(self, new_text):
        """Updates de lw_asset_categories ListWidgetItem text"""
        current_row = self.ui.lw_asset_categories_list.currentRow()
        if (current_row > -1 and current_row < self.ui.lw_asset_categories_list.count()):
            self.ui.lw_asset_categories_list.currentItem().setText(new_text)

    def description_changed(self):
        # QPlainTextEdit does not have textChanged(text). We must do it:
        self.__asset_categories[self.ui.lw_asset_categories_list.currentRow()].set_description(self.ui.plainTextEdit_description.toPlainText())

    def opportunity_changed(self):
        # QPlainTextEdit does not have textChanged(text). We must do it:
        self.__asset_categories[self.ui.lw_asset_categories_list.currentRow()].set_opportunity_definition(self.ui.plainTextEdit_opportunities.toPlainText())
    
    def add_list_widget_item(self, asset_category : AssetCategory):
        item = QListWidgetItem()
        item.setText(asset_category.name)
        self.ui.lw_asset_categories_list.addItem(item)
        self.enable_widgets()        
        self.ui.lw_asset_categories_list.setCurrentRow(self.ui.lw_asset_categories_list.count() - 1)

    def load_asset_categories(self):
        for asset_category in self.__asset_categories:
            self.add_list_widget_item(asset_category)

    def add_asset_category(self):
        # add new asset_category and listwidgetitem
        asset_category = AssetCategory()
        self.__asset_categories.append(asset_category)
        self.add_list_widget_item(asset_category)
        self.enable_widgets()        
        self.ui.lineEdit_Name.selectAll()
        self.ui.lineEdit_Name.setFocus()

    def delete_asset_category(self):
        # delete asset_category
        row = self.ui.lw_asset_categories_list.currentRow()
        if (row > -1 and row < self.ui.lw_asset_categories_list.count()):
            self.ui.lw_asset_categories_list.takeItem(row)
            self.__asset_categories.pop(row)
        self.enable_widgets()

    def row_changed(self, row : int):        
        if (row > -1 and row < self.ui.lw_asset_categories_list.count()):
            self.ui.lineEdit_Name.setText(self.__asset_categories[row].name)
            self.ui.plainTextEdit_description.setPlainText(self.__asset_categories[row].description)
            self.ui.plainTextEdit_opportunities.setPlainText(self.__asset_categories[row].opportunity_definition)
