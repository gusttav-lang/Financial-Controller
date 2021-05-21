from PySide2.QtWidgets import QWidget, QTableWidgetItem, QVBoxLayout
from src.ui.spentInYearEditor_ui import Ui_spentInYearEditor
from src.dao.yearpredictions import YearPredictions
from src.dao.valuesinyear import ValuesInYear
from PySide2.QtCore import Qt
from src.dao.spentinmonth import SpentInMonth
from src.tools.matplotlibPieChart import CategoryPieChart


class SpentInYearEditor(QWidget):
    def __init__(self, year_predictions: YearPredictions, spent_in_month : list, spent_categories : list):
        super().__init__()
        self.ui = Ui_spentInYearEditor()
        self.ui.setupUi(self)

        # DAO:
        self.__spent_in_month_list = spent_in_month
        self.__year_predictions = year_predictions
        self.__spent_categories = spent_categories

        # load interface and connects:
        self.load_tables()
        self.make_connects()

        self.ui.lbl_ano.setText(str(year_predictions._year))
        self.setup_plot()

    def setup_plot(self):
        #if len(self.__spent_categories) > 0:
        chart = CategoryPieChart(self.__spent_categories, self)
        layout = QVBoxLayout(self.ui.widget_chart)        
        layout.addWidget(chart,1)

        # sum spent in each category for the plot:
        sum_list_for_chart = []
        for category in self.__spent_categories:
            sum = 0.0
            for spent_month in self.__spent_in_month_list:
                if spent_month.year == self.__year_predictions._year:                    
                    for spent in spent_month.spent_list:
                        if spent.category == category:
                            sum += spent.how_much
                    for fixed_spent in spent_month.fixed_spent:
                        if fixed_spent.category == category:
                            sum += fixed_spent.how_much
            sum_list_for_chart.append(sum)
        chart.plot(sum_list_for_chart, True)

    def make_connects(self):        
        self.ui.tableWidget_earnings.cellChanged.connect(self.earnings_cell_changed)
        self.ui.tableWidget_spent.cellChanged.connect(self.spent_cell_changed)

    def load_tables(self):
        self.load_earnings_table()
        self.load_spent_table()       

    def load_earnings_table(self):
        number_of_line = 10
        self.ui.tableWidget_earnings.setRowCount(number_of_line)
        while (len(self.__year_predictions._earning_list) < number_of_line):
            new_value_in_year = ValuesInYear()
            self.__year_predictions._earning_list.append(new_value_in_year)
        current_row = 0

        for value_in_year in self.__year_predictions._earning_list:
            twi_where = QTableWidgetItem()
            twi_where.setData(Qt.DisplayRole, value_in_year.where)
            self.ui.tableWidget_earnings.setItem(current_row, 0, twi_where)
            twi_how_much = QTableWidgetItem()
            twi_how_much.setData(Qt.DisplayRole, value_in_year.how_much)
            self.ui.tableWidget_earnings.setItem(current_row, 1, twi_how_much)
            twi_how_parcels = QTableWidgetItem()
            twi_how_parcels.setData(Qt.DisplayRole, value_in_year.parcels)
            self.ui.tableWidget_earnings.setItem(current_row, 2, twi_how_parcels)
            twi_sum = QTableWidgetItem()
            twi_sum.setFlags(Qt.ItemIsEnabled) # Disable for edition
            self.ui.tableWidget_earnings.setItem(current_row, 3, twi_sum)
            current_row += 1
    
    def load_spent_table(self):        
        number_of_line = 10
        self.ui.tableWidget_spent.setRowCount(number_of_line)
        while (len(self.__year_predictions._spent_list) < number_of_line):
            new_value_in_year = ValuesInYear()
            self.__year_predictions._spent_list.append(new_value_in_year)
        current_row = 0

        for value_in_year in self.__year_predictions._spent_list:
            twi_where = QTableWidgetItem()
            twi_where.setData(Qt.DisplayRole, value_in_year.where)
            self.ui.tableWidget_spent.setItem(current_row, 0, twi_where)
            twi_how_much = QTableWidgetItem()
            twi_how_much.setData(Qt.DisplayRole, value_in_year.how_much)
            self.ui.tableWidget_spent.setItem(current_row, 1, twi_how_much)
            twi_how_parcels = QTableWidgetItem()
            twi_how_parcels.setData(Qt.DisplayRole, value_in_year.parcels)
            self.ui.tableWidget_spent.setItem(current_row, 2, twi_how_parcels)
            twi_sum = QTableWidgetItem()
            twi_sum.setFlags(Qt.ItemIsEnabled) # Disable for edition
            self.ui.tableWidget_spent.setItem(current_row, 3, twi_sum)
            current_row += 1

    def earnings_cell_changed(self, row : int, column : int):
        if (column == 0):
            self.__year_predictions._earning_list[row].set_where(self.ui.tableWidget_earnings.item(row, column).data(Qt.DisplayRole))
        if (column == 1):            
            self.__year_predictions._earning_list[row].set_how_much(float(self.ui.tableWidget_earnings.item(row, column).data(Qt.DisplayRole)))
            self.sum_earnings()
        if (column == 2):
            self.__year_predictions._earning_list[row].set_parcels(int(self.ui.tableWidget_earnings.item(row, column).data(Qt.DisplayRole)))
            self.sum_earnings()
    
    def spent_cell_changed(self, row : int, column : int):
        if (column == 0):
            self.__year_predictions._spent_list[row].set_where(self.ui.tableWidget_spent.item(row, column).data(Qt.DisplayRole))
        if (column == 1):            
            self.__year_predictions._spent_list[row].set_how_much(float(self.ui.tableWidget_spent.item(row, column).data(Qt.DisplayRole)))
            self.sum_spent()
        if (column == 2):
            self.__year_predictions._spent_list[row].set_parcels(int(self.ui.tableWidget_spent.item(row, column).data(Qt.DisplayRole)))
            self.sum_spent()
    
    def sum_earnings(self):
        sum = 0
        row = 0
        for year_predictions in self.__year_predictions._earning_list:
            how_much = year_predictions.how_much
            parcels = year_predictions.parcels
            if (how_much is not None and parcels is not None):
                self.ui.tableWidget_earnings.item(row,3).setData(Qt.DisplayRole, str(how_much * parcels))
                sum += how_much * parcels
            row += 1
        self.ui.lbl_sum_earnings.setText(str(sum))
        
    
    def sum_spent(self):
        sum = 0
        row = 0
        for year_predictions in self.__year_predictions._spent_list:
            how_much = year_predictions.how_much
            parcels = year_predictions.parcels
            if (how_much is not None and parcels is not None):
                self.ui.tableWidget_spent.item(row,3).setData(Qt.DisplayRole, str(how_much * parcels))
                sum += how_much * parcels
            row += 1
        self.ui.lbl_sum_spent.setText(str(sum))