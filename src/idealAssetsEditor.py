# Qt:
from PySide2.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QVBoxLayout
from PySide2.QtCore import Qt, QDate, QLocale
from PySide2.QtGui import QDoubleValidator
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
    str_today_chart_title = "Distribuição de ativos atuais"
    str_ideal_chart_title = "Distribuição de ativos ideais"
    def __init__(self, assets_in_dates_list, ideal_assets_list, asset_categories, emergency_reserves):
        super().__init__()
        self.ui = Ui_idealAssetsEditor()
        self.ui.setupUi(self)

        # DAO:
        self.__assets_in_dates_list = assets_in_dates_list
        self.__ideal_assets_list = ideal_assets_list
        self.__asset_categories = asset_categories
        self.__emergency_reserves = emergency_reserves

        self.setup_plots()

        # load interface and connects:
        self.load_tables()
        self.load_lineedits_with_validators()
        self.make_connects()

    def load_lineedits_with_validators(self):
        self.ui.lineEdit_reserva_atual.setText(str(self.__emergency_reserves.current_value))
        self.ui.lineEdit_reserva_ideal.setText(str(self.__emergency_reserves.ideal_value))
        ''' I've commented this code, since no other place uses validators (except inbuild table delegate validator)
        double_validator = QDoubleValidator()
        double_validator.setDecimals(2)
        double_validator.setNotation(QDoubleValidator.StandardNotation)  # Remove scientific notation
        current_locale = QLocale.system()
        #locale.setDefault
        double_validator.setLocale(current_locale)
        self.ui.lineEdit_reserva_atual.setValidator(double_validator)
        self.ui.lineEdit_reserva_ideal.setValidator(double_validator)'''
        
        if self.ui.lineEdit_reserva_atual.text() == 'None':
            self.ui.lineEdit_reserva_atual.setText("")
        if self.ui.lineEdit_reserva_ideal.text() == 'None':
            self.ui.lineEdit_reserva_ideal.setText("")

    def setup_plots(self):
        self.today_chart = CategoryPieChart(self.__asset_categories, self, IdealAssetsEditor.str_today_chart_title)
        layout1 = QVBoxLayout(self.ui.frame_graph_today)        
        layout1.addWidget(self.today_chart,1)
        
        self.ideal_chart = CategoryPieChart(self.__asset_categories, self, IdealAssetsEditor.str_ideal_chart_title)
        layout2 = QVBoxLayout(self.ui.frame_graph_ideal)        
        layout2.addWidget(self.ideal_chart,1)

    def make_connects(self):        
        self.ui.tableWidget_today.cellChanged.connect(self.today_cell_changed)
        self.ui.tableWidget_ideal.cellChanged.connect(self.ideal_cell_changed)
        self.ui.btn_add.clicked.connect(self.btn_add)
        self.ui.btn_delete.clicked.connect(self.btn_delete)
        self.ui.tableWidget_today.cellClicked.connect(self.today_cell_clicked)
        self.ui.lineEdit_reserva_atual.textChanged.connect(lambda x: self.__emergency_reserves.set_current_value(x))
        self.ui.lineEdit_reserva_ideal.textChanged.connect(lambda x: self.__emergency_reserves.set_ideal_value(x))

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

        # Must update labels in chart since we can have a removed category:
        headers_without_Dia = headers.copy()
        headers_without_Dia.remove("Dia")
        self.today_chart.update_category_labels(headers_without_Dia)
                
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

        self.update_today_plot(0)

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
                QMessageBox.warning(self, "Aviso", "A categoria '" + ideal_asset.category.name+ "' foi removida. Reveja seus ativos ideais!",
                                        QMessageBox.Ok)

        # Complete the table. If item does not exist, create it:
        for column, category_name in enumerate(headers):
            exist_ideal_asset_for_category = False
            for ideal_asset in self.__ideal_assets_list:
                if ideal_asset.category.name == category_name:
                    exist_ideal_asset_for_category = True
                    self.ui.tableWidget_ideal.item(0, column).setData(Qt.DisplayRole, ideal_asset.min_value)
                    self.ui.tableWidget_ideal.item(1, column).setData(Qt.DisplayRole, ideal_asset.ideal_value)
                    self.ui.tableWidget_ideal.item(2, column).setData(Qt.DisplayRole, ideal_asset.max_value)
                    break
            if not exist_ideal_asset_for_category:
                new_ideal_asset = IdealAssets()
                new_ideal_asset.set_category(self.__asset_categories[column])
                self.__ideal_assets_list.append(new_ideal_asset)
        
        self.update_ideal_plot()

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
        # Find the correct ideal asset:
        changed_category = self.__asset_categories[column]
        for ideal_asset in self.__ideal_assets_list:
            if ideal_asset.category == changed_category:
                if row == 0:
                    ideal_asset.set_min_value(self.ui.tableWidget_ideal.item(row, column).data(Qt.DisplayRole))
                elif row == 1:
                    ideal_asset.set_ideal_value(self.ui.tableWidget_ideal.item(row, column).data(Qt.DisplayRole))
                    self.update_ideal_plot()
                elif row == 2:
                    ideal_asset.set_max_value(self.ui.tableWidget_ideal.item(row, column).data(Qt.DisplayRole))

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

    def update_ideal_plot(self):
        values_list = []
        for asset_category in self.__asset_categories:
            for ideal_asset in self.__ideal_assets_list:
                if ideal_asset.category.name == asset_category.name:
                    if ideal_asset.ideal_value == None:
                        values_list.append(0)
                    else:
                        values_list.append(ideal_asset.ideal_value)
        self.ideal_chart.plot(values_list)

    def today_cell_clicked(self, row : int, column : int):
        self.update_today_plot(row)

    def update_today_plot(self, row = 0):
        if self.ui.tableWidget_today.rowCount() > row:
            date_str = self.ui.tableWidget_today.item(row, 0).data(Qt.DisplayRole).toPython().strftime("%d/%m/%Y")
            self.today_chart.update_title(IdealAssetsEditor.str_today_chart_title + " - " + date_str)
            values_list = []
            for j in range(1, self.ui.tableWidget_today.columnCount()):
                cell_value = self.ui.tableWidget_today.item(row, j).data(Qt.DisplayRole)
                if cell_value == None:
                    values_list.append(0)
                else:
                    values_list.append(cell_value)
            self.today_chart.plot(values_list)
