from PySide2.QtWidgets import QWidget, QListWidgetItem
from src.ui.assetEditor_ui import Ui_assetsEditor
from PySide2.QtCore import Qt, QDate
from src.dao.project import Project
from src.dao.objective import Objective
from src.dao.asset import Asset
from src.dao.broker import Broker
from src.dao.assetcategory import AssetCategory


class AssetsEditor(QWidget):
    def __init__(self, assets, brokers, objectives, categories):
        super().__init__()
        self.ui = Ui_assetsEditor()
        self.ui.setupUi(self)

        # DAO:
        self.__assets = assets
        self.__objectives = objectives
        self.__brokers = brokers
        self.__categories = categories

        # load interface and connects:
        self.load_assets()
        self.load_comboboxes_itens()
        self.make_connects()        

        # check if can enable delete button
        self.enable_widgets()

        if (self.ui.lw_assets_list.count() > 0):
            self.ui.lw_assets_list.setCurrentRow(-1) # corrects a bug for when there is only 1 item in the list
            self.ui.lw_assets_list.setCurrentRow(0)

    def enable_widgets(self):
        if (self.ui.lw_assets_list.count() == 0):
            self.ui.btn_delete.setEnabled(False)
            self.ui.lineEdit_Name.setEnabled(False)
            self.ui.comboBox_brokers.setEnabled(False)
            self.ui.dateEdit_purchase_day.setEnabled(False)
            self.ui.dateEdit_expiration_day.setEnabled(False)
            self.ui.lineEdit_interest.setEnabled(False)
            self.ui.lineEdit_applied_money.setEnabled(False)
            self.ui.comboBox_objectives.setEnabled(False)
            self.ui.comboBox_categories.setEnabled(False)
        else:            
            self.ui.btn_delete.setEnabled(True)
            self.ui.lineEdit_Name.setEnabled(True)
            self.ui.comboBox_brokers.setEnabled(True)
            self.ui.dateEdit_purchase_day.setEnabled(True)
            self.ui.dateEdit_expiration_day.setEnabled(True)
            self.ui.lineEdit_interest.setEnabled(True)
            self.ui.lineEdit_applied_money.setEnabled(True)
            self.ui.comboBox_objectives.setEnabled(True)
            self.ui.comboBox_categories.setEnabled(True)

    def make_connects(self):
        self.ui.btn_add.clicked.connect(self.add_asset)
        self.ui.btn_delete.clicked.connect(self.delete_asset)
        self.ui.lw_assets_list.currentRowChanged.connect(self.row_changed)
        self.ui.lineEdit_Name.textChanged.connect(self.name_changed)
        self.ui.lineEdit_Name.textChanged.connect(lambda x: self.__assets[self.ui.lw_assets_list.currentRow()].set_name(x))
        self.ui.comboBox_brokers.currentIndexChanged.connect(lambda x: self.__assets[self.ui.lw_assets_list.currentRow()].set_broker(self.__brokers[x]))
        self.ui.dateEdit_purchase_day.editingFinished.connect(self.purchase_day_edited)
        self.ui.dateEdit_expiration_day.editingFinished.connect(self.expiration_day_edited)
        self.ui.lineEdit_interest.textChanged.connect(lambda x: self.__assets[self.ui.lw_assets_list.currentRow()].set_interest(x))
        self.ui.lineEdit_applied_money.textChanged.connect(lambda x: self.__assets[self.ui.lw_assets_list.currentRow()].set_applied_money(float(x)))
        self.ui.comboBox_objectives.currentIndexChanged.connect(lambda x: self.__assets[self.ui.lw_assets_list.currentRow()].set_objective(self.__objectives[x]))
        self.ui.comboBox_categories.currentIndexChanged.connect(lambda x: self.__assets[self.ui.lw_assets_list.currentRow()].set_category(self.__categories[x]))

    def name_changed(self, new_text):
        """Updates de lw_assets ListWidgetItem text"""
        current_row = self.ui.lw_assets_list.currentRow()
        if (current_row > -1 and current_row < self.ui.lw_assets_list.count()):
            self.ui.lw_assets_list.currentItem().setText(new_text)

    def purchase_day_edited(self):
        current_row = self.ui.lw_assets_list.currentRow()
        if (current_row > -1 and current_row < self.ui.lw_assets_list.count()):
            self.__assets[current_row].set_purchase_day(self.ui.dateEdit_purchase_day.date().toPython())
    
    def expiration_day_edited(self):
        current_row = self.ui.lw_assets_list.currentRow()
        if (current_row > -1 and current_row < self.ui.lw_assets_list.count()):
            self.__assets[current_row].set_expiration_day(self.ui.dateEdit_expiration_day.date().toPython())

    def add_list_widget_item(self, asset : Asset):
        item = QListWidgetItem()
        item.setText(asset.name)
        self.ui.lw_assets_list.addItem(item)
        self.enable_widgets()
        self.ui.lw_assets_list.setCurrentRow(self.ui.lw_assets_list.count() - 1)

    def load_assets(self):
        for asset in self.__assets:
            self.add_list_widget_item(asset)

    def add_asset(self):
        # add new asset and listwidgetitem
        asset = Asset()
        self.__assets.append(asset)
        self.add_list_widget_item(asset)
        self.enable_widgets()
        self.ui.lineEdit_Name.selectAll()
        self.ui.lineEdit_Name.setFocus()

    def delete_asset(self):
        # delete asset
        row = self.ui.lw_assets_list.currentRow()
        if (row > -1 and row < self.ui.lw_assets_list.count()):
            self.ui.lw_assets_list.takeItem(row)
            self.__assets.pop(row)
        self.enable_widgets()

    def row_changed(self, row : int):        
        if (row > -1 and row < self.ui.lw_assets_list.count()):
            self.ui.lineEdit_Name.setText(self.__assets[row].name)
            self.ui.comboBox_brokers.setCurrentIndex(self.get_broker_index(self.__assets[row].broker))
            year_pd = self.__assets[row].purchase_day.year
            month_pd = self.__assets[row].purchase_day.month
            day_pd = self.__assets[row].purchase_day.day
            self.ui.dateEdit_purchase_day.setDate(QDate(year_pd, month_pd, day_pd))
            year_ed = self.__assets[row].expiration_day.year
            month_ed = self.__assets[row].expiration_day.month
            day_ed = self.__assets[row].expiration_day.day
            self.ui.dateEdit_expiration_day.setDate(QDate(year_ed, month_ed, day_ed))
            self.ui.lineEdit_interest.setText(self.__assets[row].interest)
            self.ui.lineEdit_applied_money.setText(str(self.__assets[row].applied_money))
            self.ui.comboBox_objectives.setCurrentIndex(self.get_objective_index(self.__assets[row].objective))
            self.ui.comboBox_categories.setCurrentIndex(self.get_category_index(self.__assets[row].category))

    def load_comboboxes_itens(self):
        for broker in self.__brokers:
            self.ui.comboBox_brokers.addItem(broker.name)
        for objective in self.__objectives:
            self.ui.comboBox_objectives.addItem(objective.name)
        for category in self.__categories:
            self.ui.comboBox_categories.addItem(category.name)

    def get_broker_index(self, broker : Broker):
        """Return the index in self.__brokers of broker"""
        if broker is None:
            return 0

        for i in range(len(self.__brokers)):
            if (broker is self.__brokers[i]):
                return i
        return 0

    def get_objective_index(self, objective : Objective):
        """Return the index in self.__objectives of objective"""
        if objective is None:
            return 0

        for i in range(len(self.__objectives)):
            if (objective is self.__objectives[i]):
                return i
        return 0

    def get_category_index(self, category : AssetCategory):
        """Return the index in self.__objectives of objective"""
        if category is None:
            return 0

        for i in range(len(self.__categories)):
            if (category is self.__categories[i]):
                return i
        return 0
