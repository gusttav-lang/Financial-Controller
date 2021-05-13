# Qt:
from PySide2.QtWidgets import QWidget, QTableWidgetItem
from PySide2.QtCore import Qt
from src.ui.idealAssetsEditor_ui import Ui_idealAssetsEditor
# DAO:
from src.dao.assetsinmonth import AssetsInMonth
from src.dao.idealassets import IdealAssets
from src.dao.assetcategory import AssetCategory
# Tools:
from src.tools.matplotlibPieChart import CategoryPieChart
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
        self.ui.tableWidget_today.setColumnCount(len(self.__asset_categories) + 1)  # TODO: passar pra baixo e pegar len(headers)? Se sim fazer o mesmo no spentInMonthEditor
        headers = ["Dia"]
        for asset_category in self.__asset_categories:
            headers.append(asset_category.name)
        for asset_in_month in self.__assets_in_dates_list:
            if asset_in_month.category.name not in headers:  # check for categories that were added in the month and excluded after that
                headers.append(asset_in_month.category.name) 
                self.__asset_categories.append(asset_in_month.category) # TODO: precisa disso? nao vai adicionar na lista de novo? verificar aqui e no spentInMOnthEditor
        self.ui.tableWidget_today.setHorizontalHeaderLabels(headers)

        for asset_in_month in self.__assets_in_dates_list:
            self.add_asset_in_month_to_table(asset_in_month)

    def add_asset_in_month_to_table(self, asset_in_month : AssetsInMonth):
        # find first empty line:
        first_empty_line = -1
        for i in range(self.ui.tableWidget_today.rowCount()):
            if self.ui.tableWidget_today.item(i, 0).data(Qt.DisplayRole) == None:
                first_empty_line = i
                break
        
        # search the line, if does not exist, add a new one:
        line_of_asset_in_month = -1
        for i in range(self.ui.tableWidget_today.rowCount()):
            if asset_in_month.checked_day == self.ui.tableWidget_today.item(i, 0).data(Qt.DisplayRole):
                line_of_asset_in_month = i
                break
        if line_of_asset_in_month == -1:
            line_of_asset_in_month = first_empty_line
            self.ui.tableWidget_today.item(first_empty_line, 0).setData(Qt.DisplayRole, asset_in_month.checked_day)

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
        self.ui.tableWidget_today.setHorizontalHeaderLabels(headers)

        # check if a category was excluded:



    def today_cell_changed(self, row : int, column : int):
        # parei aqui, verificar essa função. vai dar problema na conversão de QDate pra datetime
        if column == 0:
            days = []
            for i in range(self.ui.tableWidget_today.rowCount()):
                days.append(self.ui.tableWidget_today.item(i, 0).data(Qt.DisplayRole))

            # find out excluded day:
            excluded_day = -1
            for asset_in_month in self.__spent_in_month.assets_in_month:
                if asset_in_month.checked_day not in days:
                    excluded_day = asset_in_month.checked_day
                    break

            # update excluded day for new day in the correspondent assets
            for asset_in_month in self.__spent_in_month.assets_in_month:
                if asset_in_month.checked_day == excluded_day:
                    asset_in_month.set_checked_day_as_datetime(self.ui.tableWidget_today.item(row, 0).data(Qt.DisplayRole))
            
        elif column > 0:
            checked_day = self.ui.tableWidget_today.item(row, 0).data(Qt.DisplayRole)
            if checked_day != None:
                asset_category = None
                for category in self.__asset_categories:
                    if self.ui.tableWidget_today.horizontalHeaderItem(column).text() == category.name:
                        asset_category = category
                        break
                if asset_category != None:
                    asset_in_month_is_already_in_list = False
                    for asset_in_month in self.__spent_in_month.assets_in_month:
                        if asset_in_month.checked_day == checked_day and asset_in_month.category == asset_category:
                            asset_in_month_is_already_in_list = True
                            asset_in_month.set_value(self.ui.tableWidget_today.item(row, column).data(Qt.DisplayRole))
                            break
                    if asset_in_month_is_already_in_list == False:  # if asset does not already exist, create a new one
                        asset_in_month = AssetsInMonth()
                        asset_in_month.set_category(asset_category)
                        asset_in_month.set_checked_day_as_datetime(checked_day)
                        asset_in_month.set_value(self.ui.tableWidget_today.item(row, column).data(Qt.DisplayRole))
                        self.__spent_in_month.assets_in_month.append(asset_in_month)

    def ideal_cell_changed(self, row : int, column : int):
        pass

    def btn_add(self):
        self.ui.tableWidget_today.insertRow(0)
        today_date = datetime.date.today()
        for j in range(len(self.ui.tableWidget_today.columnCount())):
            twi = QTableWidgetItem()
            self.ui.tableWidget_values.setItem(0, j+1, twi)
            if (j < len(self.__asset_categories)):  # just add AssetsInMonth for non deleted Categories
                new_asset_in_month = AssetsInMonth()
                new_asset_in_month.set_checked_day_as_datetime(today_date)
                new_asset_in_month.set_category(self.__asset_categories[j])
                self.__assets_in_dates_list.append(new_asset_in_month)
            else:
                twi.setFlags(Qt.ItemIsEnabled) # Disable for edition

    def btn_delete(self):
        pass
