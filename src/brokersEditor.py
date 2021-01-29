from PySide2.QtWidgets import QWidget, QListWidgetItem
from src.ui.brokersEditor_ui import Ui_brokersEditor
from PySide2.QtCore import Qt
from src.dao.project import Project
from src.dao.broker import Broker


class BrokersEditor(QWidget):
    def __init__(self, brokers):
        super().__init__()
        self.ui = Ui_brokersEditor()
        self.ui.setupUi(self)

        # DAO:
        self.__brokers = brokers

        # load interface and connects:
        self.load_brokers()
        self.make_connects()

    def make_connects(self):
        self.ui.btn_add.clicked.connect(self.add_broker)
        self.ui.btn_delete.clicked.connect(self.delete_broker)
        self.ui.lw_brokers_list.currentRowChanged.connect(self.row_changed)
        self.ui.lineEdit_Name.textChanged.connect(self.name_changed)
        self.ui.lineEdit_bank_number.textChanged.connect(lambda x: self.__brokers[self.ui.lw_brokers_list.currentRow()].bank_number(int(x)))

    def name_changed(self, new_text):
        current_row = self.ui.lw_brokers_list.currentRow()
        if (current_row > -1 and current_row < self.ui.lw_brokers_list.count()):
            self.__brokers[current_row].name = new_text
            self.ui.lw_brokers_list.currentItem().setText(new_text)
    
    def add_list_widget_item(self, broker : Broker):
        item = QListWidgetItem()
        item.setText(broker.name)
        self.ui.lw_brokers_list.addItem(item)        

    def load_brokers(self):
        for broker in self.__brokers:
            self.add_list_widget_item(broker)

    def add_broker(self):
        # add new broker and listwidgetitem
        broker = Broker()
        self.__brokers.append(broker)
        self.add_list_widget_item(broker)

    def delete_broker(self):
        # delete broker 
        row = self.ui.lw_brokers_list.currentRow()
        self.__brokers.remove(row)
        self.ui.lw_brokers_list.removeItemWidget(self.ui.lw_brokers_list.currentItem)

    def row_changed(self, row : int):
        self.ui.lineEdit_Name.setText(self.__brokers[row].name)
        self.ui.lineEdit_bank_number.setText(str(self.__brokers[row].bank_number))
        self.ui.plainTextEdit_description.setPlainText(self.__brokers[row].description)