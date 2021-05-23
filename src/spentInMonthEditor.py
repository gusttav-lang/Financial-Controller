# Qt:
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QVBoxLayout, QApplication
from PySide2.QtGui import QColor, QBrush, QFont, QKeyEvent
from PySide2.QtCore import Qt
# General
from src.ui.spentInMonthEditor_ui import Ui_spentInMonthEditor
from src.globalvars import GlobalVars as gv
# DAO:
from src.dao.project import Project
from src.dao.spentcategory import SpentCategory
from src.dao.spentlimitgoal import SpentLimitGoal
from src.dao.spentinmonth import SpentInMonth
from src.dao.fixedspent import FixedSpent
from src.dao.revenueforecast import RevenueForecast
from src.dao.spent import Spent
from src.dao.spentlimitgoal import SpentLimitGoal
from src.dao.assetcategory import AssetCategory
from src.dao.assetsinmonth import AssetsInMonth
# Tools:
from src.tools.CategoryComboBoxItemDelegate import CategoryComboBoxItemDelegate
from src.tools.matplotlibPieChart import CategoryPieChart
from src.tools.doubledelegate import DoubleDelegate
from src.tools.dayinmonthdelegate import DayInMonthDelegate


class SpentInMonthEditor(QWidget):
    color_green = QColor(0, 200, 0)
    color_red = QColor(255, 0, 0)

    def __init__(self, spent_in_month: SpentInMonth, spent_categories, project_spent_limit_goal, asset_categories):
        super().__init__()
        self.ui = Ui_spentInMonthEditor()
        self.ui.setupUi(self)

        # DAO:
        self.__spent_in_month = spent_in_month
        self.__spent_categories = spent_categories
        self.__project_spent_limit_goal = project_spent_limit_goal
        self.__asset_categories = asset_categories
        
        self.setup_plot()

        if (len(spent_in_month.spent_list) == 0 and len(spent_in_month.fixed_spent) == 0
            and len(spent_in_month.revenue_forecast) == 0):
            self.load_new_month()

        # load interface and connects:
        self.load_tables()
        self.make_connects()

        self.ui.label.setText(gv.Meses[spent_in_month.month] + "/" + str(spent_in_month.year))
        self.adjust_initial_sizes()

    def adjust_initial_sizes(self):
        """Set sizes for full HD monitor"""
        self.ui.splitter_2.setSizes([90,200])
        self.ui.splitter_5.setSizes([90,200])
        self.ui.splitter.setSizes([5,350])

    def setup_plot(self):
        #if len(self.__spent_categories) > 0:
        self.chart = CategoryPieChart(self.__spent_categories, self)
        layout = QVBoxLayout(self.ui.widget_chart)        
        layout.addWidget(self.chart,1)

    def make_connects(self):
        self.ui.tableWidget_fixedSpent.cellChanged.connect(self.fixed_spent_cell_changed)
        self.ui.tableWidget_income.cellChanged.connect(self.income_cell_changed)
        self.ui.tableWidget_spent.cellChanged.connect(self.spent_cell_changed)
        self.ui.tableWidget_values.cellChanged.connect(self.values_cell_changed)
        self.ui.tableWidget_sum.cellChanged.connect(self.sum_cell_changed)

    def load_tables(self):
        self.load_fixed_spent_table()
        self.load_income_table()
        self.load_spent_table()
        self.load_values_table()
        self.load_sum_table()        

    def load_fixed_spent_table(self):
        if (len(self.__spent_in_month.fixed_spent) < 10):
            number_of_line = 10
        else:
            number_of_line = len(self.__spent_in_month.fixed_spent)
        self.ui.tableWidget_fixedSpent.setRowCount(number_of_line)
        while (len(self.__spent_in_month.fixed_spent) < number_of_line):
            new_fixed_spent = FixedSpent()
            self.__spent_in_month.fixed_spent.append(new_fixed_spent)
        current_row = 0

        # create delegates:
        cbd = CategoryComboBoxItemDelegate(self.__spent_categories, self.ui.tableWidget_fixedSpent)
        self.ui.tableWidget_fixedSpent.setItemDelegateForColumn(3,cbd)
        double_delegate = DoubleDelegate(self.ui.tableWidget_fixedSpent)
        self.ui.tableWidget_fixedSpent.setItemDelegateForColumn(1, double_delegate)
        dimd = DayInMonthDelegate(self.ui.tableWidget_fixedSpent)
        self.ui.tableWidget_fixedSpent.setItemDelegateForColumn(2, dimd)

        for fixed_spent in self.__spent_in_month.fixed_spent:
            twi_what = QTableWidgetItem()
            twi_what.setData(Qt.DisplayRole, fixed_spent.what)
            self.ui.tableWidget_fixedSpent.setItem(current_row, 0, twi_what)
            twi_how_much = QTableWidgetItem()
            twi_how_much.setData(Qt.DisplayRole, fixed_spent.how_much)
            self.ui.tableWidget_fixedSpent.setItem(current_row, 1, twi_how_much)
            twi_how_day = QTableWidgetItem()
            twi_how_day.setData(Qt.DisplayRole, fixed_spent.day_in_month)
            self.ui.tableWidget_fixedSpent.setItem(current_row, 2, twi_how_day)
            twi_category = QTableWidgetItem()
            if (fixed_spent.category != None): # just fill if has been initialized
                twi_category.setData(Qt.DisplayRole, fixed_spent.category.name)
            self.ui.tableWidget_fixedSpent.setItem(current_row, 3, twi_category)
            current_row += 1
    
    def load_income_table(self):        
        if (len(self.__spent_in_month.revenue_forecast) < 10):
            number_of_line = 10
        else:
            number_of_line = len(self.__spent_in_month.revenue_forecast)
        self.ui.tableWidget_income.setRowCount(number_of_line)
        while (len(self.__spent_in_month.revenue_forecast) < number_of_line):
            new_revenue = RevenueForecast()
            self.__spent_in_month.revenue_forecast.append(new_revenue)
        current_row = 0

        # create delegates:
        double_delegate = DoubleDelegate(self.ui.tableWidget_income)
        self.ui.tableWidget_income.setItemDelegateForColumn(1, double_delegate)
        dimd = DayInMonthDelegate(self.ui.tableWidget_income)
        self.ui.tableWidget_income.setItemDelegateForColumn(2, dimd)

        for income in self.__spent_in_month.revenue_forecast:
            twi_what = QTableWidgetItem()
            twi_what.setData(Qt.DisplayRole, income.what)
            self.ui.tableWidget_income.setItem(current_row, 0, twi_what)
            twi_how_much = QTableWidgetItem()
            twi_how_much.setData(Qt.DisplayRole, income.how_much)
            self.ui.tableWidget_income.setItem(current_row, 1, twi_how_much)
            twi_how_day = QTableWidgetItem()
            twi_how_day.setData(Qt.DisplayRole, income.day_in_month)
            self.ui.tableWidget_income.setItem(current_row, 2, twi_how_day)
            current_row += 1

        self.update_income_sum()

    def load_spent_table(self):
        if (len(self.__spent_in_month.spent_list) < 50):
            number_of_line = 50
        else:
            number_of_line = len(self.__spent_in_month.spent_list)
        self.ui.tableWidget_spent.setRowCount(number_of_line)
        while (len(self.__spent_in_month.spent_list) < number_of_line):
            new_spent = Spent()
            self.__spent_in_month.spent_list.append(new_spent)
        current_row = 0

        # create delegates:
        cbd = CategoryComboBoxItemDelegate(self.__spent_categories, self.ui.tableWidget_spent)
        self.ui.tableWidget_spent.setItemDelegateForColumn(3,cbd)
        double_delegate = DoubleDelegate(self.ui.tableWidget_spent)
        self.ui.tableWidget_spent.setItemDelegateForColumn(1, double_delegate)
        dimd = DayInMonthDelegate(self.ui.tableWidget_spent)
        self.ui.tableWidget_spent.setItemDelegateForColumn(0, dimd)

        for spent in self.__spent_in_month.spent_list:
            twi_how_day = QTableWidgetItem()
            twi_how_day.setData(Qt.DisplayRole, spent.day_in_month)
            self.ui.tableWidget_spent.setItem(current_row, 0, twi_how_day)
            twi_how_much = QTableWidgetItem()
            twi_how_much.setData(Qt.DisplayRole, spent.how_much)
            self.ui.tableWidget_spent.setItem(current_row, 1, twi_how_much)
            twi_where = QTableWidgetItem()
            twi_where.setData(Qt.DisplayRole, spent.where)
            self.ui.tableWidget_spent.setItem(current_row, 2, twi_where)
            twi_category = QTableWidgetItem()
            if (spent.category != None): # just fill if has been initialized
                twi_category.setData(Qt.DisplayRole, spent.category.name)
            self.ui.tableWidget_spent.setItem(current_row, 3, twi_category)
            current_row += 1

    def load_values_table(self):
        headers = ["Dia verificado"]
        for asset_category in self.__asset_categories:
            headers.append(asset_category.name)
        for asset_in_month in self.__spent_in_month.assets_in_month:
            if asset_in_month.category.name not in headers:  # check for categories that were added in the month and excluded after that
                headers.append(asset_in_month.category.name) 
                self.__asset_categories.append(asset_in_month.category)                
        self.ui.tableWidget_values.setColumnCount(len(headers))
        self.ui.tableWidget_values.setHorizontalHeaderLabels(headers)

        number_of_lines = 5
        self.ui.tableWidget_values.setRowCount(number_of_lines)
        for i in range(number_of_lines):
            for j in range(len(headers)):
                twi = QTableWidgetItem()
                self.ui.tableWidget_values.setItem(i, j, twi)

        for asset_in_month in self.__spent_in_month.assets_in_month:
            self.add_asset_in_month_to_table(asset_in_month)

        '''
        Here I need to make it different. I can't know if the position of the asset_in_month inside the list
        while (len(self.__spent_in_month.revenue_forecast)/(len(headers)-1) < number_of_line):
            new_asset_in_month = AssetsInMonth()
            self.__spent_in_month.assets_in_month.append(new_asset_in_month)
        current_row = 0'''

    def add_asset_in_month_to_table(self, asset_in_month : AssetsInMonth):
        # find first empty line:
        first_empty_line = -1
        for i in range(self.ui.tableWidget_values.rowCount()):
            if self.ui.tableWidget_values.item(i, 0).data(Qt.DisplayRole) == None:
                first_empty_line = i
                break
        
        # search the line, if does not exist, add a new one:
        line_of_asset_in_month = -1
        for i in range(self.ui.tableWidget_values.rowCount()):
            if asset_in_month.checked_day.day == self.ui.tableWidget_values.item(i, 0).data(Qt.DisplayRole):
                line_of_asset_in_month = i
                break
        if line_of_asset_in_month == -1:
            line_of_asset_in_month = first_empty_line
            self.ui.tableWidget_values.item(first_empty_line, 0).setData(Qt.DisplayRole, asset_in_month.checked_day.day)

        # find the correct column:
        column_of_asset_in_month = -1
        for i in range(1, self.ui.tableWidget_values.columnCount()):
            if asset_in_month.category.name == self.ui.tableWidget_values.horizontalHeaderItem(i).text():
                column_of_asset_in_month = i
                break

        self.ui.tableWidget_values.item(line_of_asset_in_month, column_of_asset_in_month).setData(Qt.DisplayRole, asset_in_month.value)

    def load_sum_table(self):
        self.check_new_categories_for_spent_limit()
        for spent_limit in self.__spent_in_month.spent_limit_goal:
            initial_row_count = self.ui.tableWidget_sum.rowCount()
            self.ui.tableWidget_sum.insertRow(initial_row_count)
            
            #create and insert QTableWidgetItems
            twi_category = QTableWidgetItem()
            twi_category.setData(Qt.DisplayRole, spent_limit.category.name)
            twi_category.setFlags(Qt.ItemIsEnabled) # Disable for edition
            self.ui.tableWidget_sum.setItem(initial_row_count, 0, twi_category)
            twi_sum = QTableWidgetItem()
            # twi_sum.setData(Qt.DisplayRole, spent_limit.category.name)
            twi_sum.setFlags(Qt.ItemIsEnabled) # Disable for edition
            self.ui.tableWidget_sum.setItem(initial_row_count, 1, twi_sum)
            twi_goal = QTableWidgetItem()
            bold_font = QFont()
            bold_font.setBold(True)
            twi_goal.setFont(bold_font)
            twi_goal.setData(Qt.DisplayRole, spent_limit.amount)
            self.ui.tableWidget_sum.setItem(initial_row_count, 2, twi_goal)
        self.update_spent_sum()
        self.update_all_colors_sum_table()

    def load_new_month(self):
        self.check_new_categories_for_spent_limit() # create SpentLimitGoal objects

        # set the project_limit_goal as default
        for project_spent_limit in self.__project_spent_limit_goal:
            for spent_limit in self.__spent_in_month.spent_limit_goal:
                if (spent_limit.category == project_spent_limit.category):
                    spent_limit.set_amount(project_spent_limit.amount)
                    break
            
        # TODO:perguntar se quer importar gastos fixos, receitas e obrigar a planejar teto de gastos

    def update_spent_sum(self):
        # update all categories sum of spent
        row = 0
        sum_list_for_chart = []
        for category in self.__spent_categories:
            sum_category = 0.0
            for fixed_spent in self.__spent_in_month.fixed_spent:
                if fixed_spent.category == category:
                    if (fixed_spent.how_much != None):
                        sum_category += fixed_spent.how_much
            for spent in self.__spent_in_month.spent_list:
                if spent.category == category:
                    if (spent.how_much != None):
                        sum_category += spent.how_much
            self.ui.tableWidget_sum.item(row, 1).setData(Qt.DisplayRole, sum_category)
            row += 1
            sum_list_for_chart.append(sum_category)
        self.chart.plot(sum_list_for_chart)
        self.ui.lalbel_sum_spent.setText(str(round(sum(sum_list_for_chart), 2)))
    
    def check_new_categories_for_spent_limit(self):
        #first, check if any category was excluded:
        for spent_limit in self.__spent_in_month.spent_limit_goal:
            if (spent_limit.category not in self.__spent_categories):
                self.__spent_in_month.spent_limit_goal.remove(spent_limit) 

        #then, check if a new category was added:
        for category in self.__spent_categories:
            is_in_category = False
            for spent_limit in self.__spent_in_month.spent_limit_goal:
                if (category == spent_limit.category):
                    is_in_category = True
                    break
            if (is_in_category == False):
                new_goal = SpentLimitGoal()
                new_goal.set_category(category)
                self.__spent_in_month.spent_limit_goal.append(new_goal)

    def fixed_spent_cell_changed(self, row : int, column : int):
        if (column == 0):
            self.__spent_in_month.fixed_spent[row].set_what(self.ui.tableWidget_fixedSpent.item(row, column).data(Qt.DisplayRole))
        if (column == 1):
            self.__spent_in_month.fixed_spent[row].set_how_much(self.ui.tableWidget_fixedSpent.item(row, column).data(Qt.DisplayRole))
            self.update_spent_sum()
        if (column == 2):
            self.__spent_in_month.fixed_spent[row].set_day_in_month(self.ui.tableWidget_fixedSpent.item(row, column).data(Qt.DisplayRole))
        if (column == 3):
            category = SpentCategory.get_category_by_name(self.ui.tableWidget_fixedSpent.item(row, column).data(Qt.DisplayRole), self.__spent_categories)
            self.__spent_in_month.fixed_spent[row].set_category(category)
            self.update_spent_sum()
    
    def income_cell_changed(self, row : int, column : int):
        if (column == 0):
            self.__spent_in_month.revenue_forecast[row].set_what(self.ui.tableWidget_income.item(row, column).data(Qt.DisplayRole))
        if (column == 1):
            self.__spent_in_month.revenue_forecast[row].set_how_much(self.ui.tableWidget_income.item(row, column).data(Qt.DisplayRole))
        if (column == 2):
            self.__spent_in_month.revenue_forecast[row].set_day_in_month(self.ui.tableWidget_income.item(row, column).data(Qt.DisplayRole))
        self.update_income_sum()

    def update_income_sum(self):
        income_sum = 0
        for income in self.__spent_in_month.revenue_forecast:
            if income.how_much != None:
                income_sum += income.how_much
        self.ui.label_sum_earnings.setText(str(round(income_sum, 2)))

    def spent_cell_changed(self, row : int, column : int):
        if (column == 0):
            self.__spent_in_month.spent_list[row].set_day(self.ui.tableWidget_spent.item(row, column).data(Qt.DisplayRole), self.__spent_in_month.month, self.__spent_in_month.year)            
        if (column == 1):
            self.__spent_in_month.spent_list[row].set_how_much(self.ui.tableWidget_spent.item(row, column).data(Qt.DisplayRole))
            self.update_spent_sum()
        if (column == 2):
            self.__spent_in_month.spent_list[row].set_where(self.ui.tableWidget_spent.item(row, column).data(Qt.DisplayRole))
        if (column == 3):
            category = SpentCategory.get_category_by_name(self.ui.tableWidget_spent.item(row, column).data(Qt.DisplayRole), self.__spent_categories)
            self.__spent_in_month.spent_list[row].set_category(category)
            self.update_spent_sum()
    
    def values_cell_changed(self, row : int, column : int):
        if column == 0:
            days = []
            for i in range(self.ui.tableWidget_values.rowCount()):
                days.append(self.ui.tableWidget_values.item(i, 0).data(Qt.DisplayRole))

            # find out excluded day:
            excluded_day = -1
            for asset_in_month in self.__spent_in_month.assets_in_month:
                if asset_in_month.checked_day.day not in days:
                    excluded_day = asset_in_month.checked_day.day
                    break

            # update excluded day for new day in the correspondent assets
            for asset_in_month in self.__spent_in_month.assets_in_month:
                if asset_in_month.checked_day.day == excluded_day:
                    asset_in_month.set_checked_day(self.ui.tableWidget_values.item(row, 0).data(Qt.DisplayRole), self.__spent_in_month.month, self.__spent_in_month.year)
            
        elif column > 0:
            checked_day = self.ui.tableWidget_values.item(row, 0).data(Qt.DisplayRole)
            if checked_day != None:
                asset_category = None
                for category in self.__asset_categories:
                    if self.ui.tableWidget_values.horizontalHeaderItem(column).text() == category.name:
                        asset_category = category
                        break
                if asset_category != None:
                    asset_in_month_is_already_in_list = False
                    for asset_in_month in self.__spent_in_month.assets_in_month:
                        if asset_in_month.checked_day.day == checked_day and asset_in_month.category == asset_category:
                            asset_in_month_is_already_in_list = True
                            asset_in_month.set_value(self.ui.tableWidget_values.item(row, column).data(Qt.DisplayRole))
                            break
                    if asset_in_month_is_already_in_list == False:  # if asset does not already exist, create a new one
                        asset_in_month = AssetsInMonth()
                        asset_in_month.set_category(asset_category)
                        asset_in_month.set_checked_day(checked_day, self.__spent_in_month.month, self.__spent_in_month.year)
                        asset_in_month.set_value(self.ui.tableWidget_values.item(row, column).data(Qt.DisplayRole))
                        self.__spent_in_month.assets_in_month.append(asset_in_month)
    
    def sum_cell_changed(self, row : int, column : int):
        if (column == 2):
            self.__spent_in_month.spent_limit_goal[row].set_amount(self.ui.tableWidget_sum.item(row, column).data(Qt.DisplayRole))  
        self.update_row_color_sum_table(row)    

    def update_all_colors_sum_table(self):
        for row in range(self.ui.tableWidget_sum.rowCount()):
            self.update_row_color_sum_table(row)

    def update_row_color_sum_table(self, row : int):
        try:
            if (float(self.ui.tableWidget_sum.item(row, 1).data(Qt.DisplayRole)) <= float(self.ui.tableWidget_sum.item(row, 2).data(Qt.DisplayRole))):
                font_color = self.color_green
            else:
                font_color = self.color_red
        except:
            font_color = self.color_red
        self.ui.tableWidget_sum.item(row, 1).setForeground(QBrush(font_color)) 

    def keyPressEvent(self, event : QKeyEvent):
        super().keyPressEvent(event)

        QApplication.setOverrideCursor(Qt.WaitCursor)  # change cursor

        # Delete Key:
        if (event.key() == Qt.Key_Delete):
            current_widget = QApplication.focusWidget()
            if (current_widget == self.ui.tableWidget_fixedSpent or
                    current_widget == self.ui.tableWidget_income or
                    current_widget == self.ui.tableWidget_spent or
                    current_widget == self.ui.tableWidget_values or
                    current_widget == self.ui.tableWidget_sum):
                row_count = current_widget.rowCount()
                column_count = current_widget.columnCount()
                for item in current_widget.selectedItems():
                    row = item.row()
                    column = item.column()
                    if (row > -1 and row < row_count and column > -1 and column < column_count):
                        current_widget.item(row, column).setData(Qt.DisplayRole, None)

        # Ctrl + c:
        if (event.key() == Qt.Key_C and event.modifiers() == Qt.ControlModifier):
            current_widget = QApplication.focusWidget()
            if (current_widget == self.ui.tableWidget_fixedSpent or
                    current_widget == self.ui.tableWidget_income or
                    current_widget == self.ui.tableWidget_spent or
                    current_widget == self.ui.tableWidget_values or
                    current_widget == self.ui.tableWidget_sum):                
                items = current_widget.selectedItems()
                text = ""
                previous_row = -1
                for item in items:
                    current_row = item.row()
                    if (previous_row == -1):
                        pass                
                    elif (current_row == previous_row):
                        text += "\t"
                    elif (current_row == previous_row + 1):
                        text += "\n"

                    if (item.data(Qt.DisplayRole) != None):
                        text += str(item.data(Qt.DisplayRole))
                    previous_row = item.row()

                QApplication.clipboard().setText(text)

        # Ctrl + v:
        if (event.key() == Qt.Key_V and event.modifiers() == Qt.ControlModifier):
            current_widget = QApplication.focusWidget()
            if (current_widget == self.ui.tableWidget_fixedSpent or
                    current_widget == self.ui.tableWidget_income or
                    current_widget == self.ui.tableWidget_spent or
                    current_widget == self.ui.tableWidget_values or
                    current_widget == self.ui.tableWidget_sum):
                column_count = current_widget.columnCount()
                row_count = current_widget.rowCount()
                text = QApplication.clipboard().text()
                current_row = current_widget.currentRow()
                initial_column = current_widget.currentColumn()
                lines = text.split('\n')
                text_all_lines = []
                for line in lines:
                    cells = line.split('\t')
                    text_all_lines.append(cells)
                for line in text_all_lines:
                    if (current_row >= current_widget.rowCount()):  # check if a new line is needed
                        self.add_one_empty_lines(current_widget)
                    column = initial_column
                    for cell in line:
                        if column < column_count:
                            if (column == 3):  # check if category exists
                                is_in_spent_category = False
                                correct_name = ""  # correct name with Upper cases
                                for category in self.__spent_categories:
                                    if cell.lower() == category.name.lower():
                                        is_in_spent_category = True
                                        correct_name = category.name
                                        break
                                if (is_in_spent_category):
                                    current_widget.item(current_row, column).setData(Qt.DisplayRole, correct_name)
                            else:
                                current_widget.item(current_row, column).setData(Qt.DisplayRole, cell)
                        column += 1

                    current_row += 1

        # Insert
        if (event.key() == Qt.Key_Insert):
            current_widget = QApplication.focusWidget()
            if (current_widget == self.ui.tableWidget_fixedSpent or
                    current_widget == self.ui.tableWidget_income or
                    current_widget == self.ui.tableWidget_spent):
                self.add_one_empty_lines(current_widget)

        QApplication.restoreOverrideCursor()  # restores cursor

    def add_one_empty_lines(self, table : QWidget):
        # add line to 'table' and create item in dao list, if needed
        def create_twi(table : QWidget()):
            for j in range(table.columnCount()):
                twi = QTableWidgetItem()
                table.setItem(table.rowCount() - 1, j, twi)

        if (table == self.ui.tableWidget_fixedSpent):
            new_fixed_spent = FixedSpent()
            self.__spent_in_month.fixed_spent.append(new_fixed_spent)
            table.setRowCount(table.rowCount() + 1)
            create_twi(table)
            
        elif table == self.ui.tableWidget_income:
            new_revenue = RevenueForecast()
            self.__spent_in_month.revenue_forecast.append(new_revenue)
            table.setRowCount(table.rowCount() + 1)
            create_twi(table)
        elif table == self.ui.tableWidget_spent:
            new_spent = Spent()
            self.__spent_in_month.spent_list.append(new_spent)
            table.setRowCount(table.rowCount() + 1)
            create_twi(table)
