# Qt:
from PySide2.QtWidgets import QWidget, QTableWidgetItem
from PySide2.QtCore import Qt, QDate
from src.ui.idealAssetsEditor_ui import Ui_idealAssetsEditor
# DAO:
from src.dao.assetsinmonth import AssetsInMonth
from src.dao.idealassets import IdealAssets
from src.dao.assetcategory import AssetCategory
# Tools:
from src.tools.matplotlibPieChart import CategoryPieChart
from src.tools.dateeditdelegate import DateEditDelegate
from src.tools.doubledelegate import DoubleDelegate
# Python
import datetime


class IdealAssetsEditor(QWidget):
    def __init__(self, assets_in_dates_list, ideal_assets_list, asset_categories):
        super().__init__()
        self.ui = Ui_idealAssetsEditor()
        self.ui.setupUi(self)

        # DAO:
        self.__assets_in_dates_list = assets_in_dates_list
        self.__ideal_assets_list = ideal_assets_list
        self.__asset_categories = asset_categories

        self.setup_plot()

        # load interface and connects:
        self.load_tables()
        self.make_connects()

    def setup_plot(self):
        pass

    def make_connects(self):        
        self.ui.tableWidget_today.cellChanged.connect(self.today_cell_changed)
        self.ui.tableWidget_ideal.cellChanged.connect(self.ideal_cell_changed)
        self.ui.btn_add.clicked.connect(self.btn_add)
        self.ui.btn_delete.clicked.connect(self.btn_delete)

    def load_tables(self):
        self.load_today_table()
        self.load_ideal_table()

    def load_today_table(self):
        headers = ["Dia"]
        for asset_category in self.__asset_categories:
            headers.append(asset_category.name)
        for asset_in_month in self.__assets_in_dates_list:
            if asset_in_month.category.name not in headers:  # check for categories that were added in the month and excluded after that
                headers.append(asset_in_month.category.name) 
                #self.__asset_categories.append(asset_in_month.category) # TODO: precisa disso? nao vai adicionar na lista de novo? verificar aqui e no spentInMOnthEditor
                
        self.ui.tableWidget_today.setColumnCount(len(headers))
        ded = DateEditDelegate(self.ui.tableWidget_today)
        double_delegate = DoubleDelegate(self.ui.tableWidget_today)
        self.ui.tableWidget_today.setItemDelegateForColumn(0, ded)
        for i in range(1, self.ui.tableWidget_today.columnCount()):
            self.ui.tableWidget_today.setItemDelegateForColumn(i, double_delegate)

        self.ui.tableWidget_today.setHorizontalHeaderLabels(headers)

        # add the needed lines:
        list_of_dates = []
        for asset_in_month in self.__assets_in_dates_list:
            if asset_in_month.checked_day not in list_of_dates:
                list_of_dates.append(asset_in_month.checked_day)
                # create the line:
                self.ui.tableWidget_today.insertRow(0)
                for j in range(self.ui.tableWidget_today.columnCount()):
                    twi = QTableWidgetItem()
                    self.ui.tableWidget_today.setItem(0, j, twi)
                date_as_QDate = QDate(asset_in_month.checked_day.year, asset_in_month.checked_day.month, asset_in_month.checked_day.day)
                self.ui.tableWidget_today.item(0,0).setData(Qt.DisplayRole, date_as_QDate)

        for asset_in_month in self.__assets_in_dates_list:
            self.add_asset_in_month_to_table(asset_in_month)

    def add_asset_in_month_to_table(self, asset_in_month : AssetsInMonth):
        # find de correct line:
        line_of_asset_in_month = -1
        for i in range(self.ui.tableWidget_today.rowCount()):
            if asset_in_month.checked_day == self.ui.tableWidget_today.item(i, 0).data(Qt.DisplayRole):
                line_of_asset_in_month = i
                break

        # find the correct column:
        column_of_asset_in_month = -1
        for i in range(1, self.ui.tableWidget_today.columnCount()):
            if asset_in_month.category.name == self.ui.tableWidget_today.horizontalHeaderItem(i).text():
                column_of_asset_in_month = i
                break

        self.ui.tableWidget_today.item(line_of_asset_in_month, column_of_asset_in_month).setData(Qt.DisplayRole, asset_in_month.value)

    def load_ideal_table(self):
        headers = []
        for asset_category in self.__asset_categories:
            headers.append(asset_category.name)
        self.ui.tableWidget_ideal.setColumnCount(len(headers))
        self.ui.tableWidget_ideal.setHorizontalHeaderLabels(headers)

        # create QTableWidgetItems:
        for i in range(self.ui.tableWidget_ideal.rowCount()):
            for j in range(self.ui.tableWidget_ideal.columnCount()):
                twi = QTableWidgetItem()
                self.ui.tableWidget_ideal.setItem(i,j,twi)

        # create delegate:
        double_delegate = DoubleDelegate(self.ui.tableWidget_ideal)
        self.ui.tableWidget_ideal.setItemDelegate(double_delegate)

        # check if a category was excluded and then delete:
        for ideal_asset in reversed(self.__ideal_assets_list):
            if ideal_asset.category not in self.__asset_categories:
                self.__ideal_assets_list.remove(ideal_asset)

        # Complete the table. If item does not exist, create it:
        # Fazer um find pela celula esperada ponto a ponto



    def today_cell_changed(self, row : int, column : int):
        if column == 0:
            days = []
            for i in range(self.ui.tableWidget_today.rowCount()):
                days.append(self.ui.tableWidget_today.item(i, 0).data(Qt.DisplayRole))

            # find out excluded day:
            excluded_day = -1
            for asset_in_month in self.__assets_in_dates_list:
                if asset_in_month.checked_day not in days:
                    excluded_day = asset_in_month.checked_day
                    break

            # update excluded day for new day in the correspondent assets
            for asset_in_month in self.__assets_in_dates_list:
                if asset_in_month.checked_day == excluded_day:
                    asset_in_month.set_checked_day_as_datetime(self.ui.tableWidget_today.item(row, 0).data(Qt.DisplayRole))
            
        elif column > 0:
            checked_day = self.ui.tableWidget_today.item(row, 0).data(Qt.DisplayRole).toPython()
            if checked_day != None:
                asset_category = None
                for category in self.__asset_categories:
                    if self.ui.tableWidget_today.horizontalHeaderItem(column).text() == category.name:
                        asset_category = category
                        break
                if asset_category != None:
                    #asset_in_month_is_already_in_list = False
                    for asset_in_month in self.__assets_in_dates_list:
                        if asset_in_month.checked_day == checked_day and asset_in_month.category == asset_category:
                            #asset_in_month_is_already_in_list = True
                            asset_in_month.set_value(self.ui.tableWidget_today.item(row, column).data(Qt.DisplayRole))
                            break
                    '''if asset_in_month_is_already_in_list == False:  # if asset does not already exist, create a new one
                        asset_in_month = AssetsInMonth()
                        asset_in_month.set_category(asset_category)
                        asset_in_month.set_checked_day_as_datetime(checked_day)
                        asset_in_month.set_value(self.ui.tableWidget_today.item(row, column).data(Qt.DisplayRole))
                        self.__assets_in_dates_list.append(asset_in_month)'''

    def ideal_cell_changed(self, row : int, column : int):
        pass

    def btn_add(self):
        self.ui.tableWidget_today.insertRow(0)
        today_date = datetime.date.today() 
        today_date_as_QDate = QDate(today_date.year, today_date.month, today_date.day)       
        twi_date = QTableWidgetItem()  # add QTableWidgetItem in first column
        self.ui.tableWidget_today.setItem(0, 0, twi_date)
        twi_date.setData(Qt.DisplayRole, today_date_as_QDate)
        for j in range(1, self.ui.tableWidget_today.columnCount()):
            twi = QTableWidgetItem()
            self.ui.tableWidget_today.setItem(0, j, twi)
            if (j-1 < len(self.__asset_categories)):  # just add AssetsInMonth for non deleted Categories
                new_asset_in_month = AssetsInMonth()
                new_asset_in_month.set_checked_day_as_datetime(today_date)
                new_asset_in_month.set_category(self.__asset_categories[j-1])
                self.__assets_in_dates_list.append(new_asset_in_month)
            else:
                twi.setFlags(Qt.ItemIsEnabled) # Disable for edition

    def btn_delete(self):
        current_row = self.ui.tableWidget_today.currentRow()
        if (current_row > -1 and current_row < self.ui.tableWidget_today.rowCount()):
            day = self.ui.tableWidget_today.item(current_row,0).data(Qt.DisplayRole)
            for asset_in_month in reversed(self.__assets_in_dates_list):
                if (asset_in_month.checked_day == day):
                    self.__assets_in_dates_list.remove(asset_in_month)

            self.ui.tableWidget_today.removeRow(current_row)
