from PySide2.QtWidgets import QWidget, QListWidgetItem
from src.ui.liabilityEditor_ui import Ui_liabilitiesEditor
from PySide2.QtCore import Qt, QDate
from src.dao.project import Project
from src.dao.liability import Liability
from src.dao.broker import Broker


class LiabilitiesEditor(QWidget):
    def __init__(self, liabilities, brokers):
        super().__init__()
        self.ui = Ui_liabilitiesEditor()
        self.ui.setupUi(self)

        # DAO:
        self.__liabilities = liabilities
        self.__brokers = brokers

        # load interface and connects:
        self.load_liabilities()
        self.load_comboboxes_itens()
        self.make_connects()        

        # check if can enable delete button
        self.enable_widgets()

        if (self.ui.lw_liabilities_list.count() > 0):
            self.ui.lw_liabilities_list.setCurrentRow(-1) # corrects a bug for when there is only 1 item in the list
            self.ui.lw_liabilities_list.setCurrentRow(0)

    def enable_widgets(self):
        if (self.ui.lw_liabilities_list.count() == 0):
            self.ui.btn_delete.setEnabled(False)
            self.ui.lineEdit_Name.setEnabled(False)
            self.ui.comboBox_brokers.setEnabled(False)
            self.ui.dateEdit_purchase_day.setEnabled(False)
            self.ui.dateEdit_expiration_day.setEnabled(False)
            self.ui.lineEdit_interest.setEnabled(False)
            self.ui.lineEdit_borrowed_money.setEnabled(False)
        else:            
            self.ui.btn_delete.setEnabled(True)
            self.ui.lineEdit_Name.setEnabled(True)
            self.ui.comboBox_brokers.setEnabled(True)
            self.ui.dateEdit_purchase_day.setEnabled(True)
            self.ui.dateEdit_expiration_day.setEnabled(True)
            self.ui.lineEdit_interest.setEnabled(True)
            self.ui.lineEdit_borrowed_money.setEnabled(True)

    def make_connects(self):
        self.ui.btn_add.clicked.connect(self.add_liability)
        self.ui.btn_delete.clicked.connect(self.delete_liability)
        self.ui.lw_liabilities_list.currentRowChanged.connect(self.row_changed)
        self.ui.lineEdit_Name.textChanged.connect(self.name_changed)
        self.ui.lineEdit_Name.textChanged.connect(lambda x: self.__liabilities[self.ui.lw_liabilities_list.currentRow()].set_name(x))
        self.ui.comboBox_brokers.currentIndexChanged.connect(lambda x: self.__liabilities[self.ui.lw_liabilities_list.currentRow()].set_broker(self.__brokers[x]))
        self.ui.dateEdit_purchase_day.editingFinished.connect(self.purchase_day_edited)
        self.ui.dateEdit_expiration_day.editingFinished.connect(self.expiration_day_edited)
        self.ui.lineEdit_interest.textChanged.connect(lambda x: self.__liabilities[self.ui.lw_liabilities_list.currentRow()].set_interest(x))
        self.ui.lineEdit_borrowed_money.textChanged.connect(lambda x: self.__liabilities[self.ui.lw_liabilities_list.currentRow()].set_borrowed_money(float(x)))

    def name_changed(self, new_text):
        """Updates de lw_liabilities ListWidgetItem text"""
        current_row = self.ui.lw_liabilities_list.currentRow()
        if (current_row > -1 and current_row < self.ui.lw_liabilities_list.count()):
            self.ui.lw_liabilities_list.currentItem().setText(new_text)

    def purchase_day_edited(self):
        current_row = self.ui.lw_liabilities_list.currentRow()
        if (current_row > -1 and current_row < self.ui.lw_liabilities_list.count()):
            self.__liabilities[current_row].set_purchase_day(self.ui.dateEdit_purchase_day.date().toPython())
    
    def expiration_day_edited(self):
        current_row = self.ui.lw_liabilities_list.currentRow()
        if (current_row > -1 and current_row < self.ui.lw_liabilities_list.count()):
            self.__liabilities[current_row].set_expiration_day(self.ui.dateEdit_expiration_day.date().toPython())

    def add_list_widget_item(self, liability : Liability):
        item = QListWidgetItem()
        item.setText(liability.name)
        self.ui.lw_liabilities_list.addItem(item)
        self.enable_widgets()
        self.ui.lw_liabilities_list.setCurrentRow(self.ui.lw_liabilities_list.count() - 1)

    def load_liabilities(self):
        for liability in self.__liabilities:
            self.add_list_widget_item(liability)

    def add_liability(self):
        # add new liability and listwidgetitem
        liability = Liability()
        self.__liabilities.append(liability)
        self.add_list_widget_item(liability)
        self.enable_widgets()
        self.ui.lineEdit_Name.selectAll()
        self.ui.lineEdit_Name.setFocus()

    def delete_liability(self):
        # delete liability
        row = self.ui.lw_liabilities_list.currentRow()
        if (row > -1 and row < self.ui.lw_liabilities_list.count()):
            self.ui.lw_liabilities_list.takeItem(row)
            self.__liabilities.pop(row)
        self.enable_widgets()

    def row_changed(self, row : int):        
        if (row > -1 and row < self.ui.lw_liabilities_list.count()):
            self.ui.lineEdit_Name.setText(self.__liabilities[row].name)
            self.ui.comboBox_brokers.setCurrentIndex(self.get_broker_index(self.__liabilities[row].broker))
            year_pd = self.__liabilities[row].purchase_day.year
            month_pd = self.__liabilities[row].purchase_day.month
            day_pd = self.__liabilities[row].purchase_day.day
            self.ui.dateEdit_purchase_day.setDate(QDate(year_pd, month_pd, day_pd))
            year_ed = self.__liabilities[row].expiration_day.year
            month_ed = self.__liabilities[row].expiration_day.month
            day_ed = self.__liabilities[row].expiration_day.day
            self.ui.dateEdit_expiration_day.setDate(QDate(year_ed, month_ed, day_ed))
            self.ui.lineEdit_interest.setText(self.__liabilities[row].interest)
            self.ui.lineEdit_borrowed_money.setText(str(self.__liabilities[row].borrowed_money))

    def load_comboboxes_itens(self):
        for broker in self.__brokers:
            self.ui.comboBox_brokers.addItem(broker.name)

    def get_broker_index(self, broker : Broker):
        """Return the index in self.__brokers of broker"""
        if broker is None:
            return 0

        for i in range(len(self.__brokers)):
            if (broker is self.__brokers[i]):
                return i
        return 0

