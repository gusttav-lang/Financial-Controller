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
        self.loadBrokers()
        self.ui.btn_add.clicked.connect(self.add_broker)
        self.ui.btn_delete.clicked.connect(self.delete_broker)

    def add_list_widget_item(self, broker : Broker):
        item = QListWidgetItem()
        item.setText(broker.name())
        self.ui.lw_brokers_list.addItem(item)
        

    def loadBrokers(self):
        for broker in self.__brokers:
            self.add_list_widget_item(broker)

    def add_broker(self):
        # add new broker and listwidgetitem
        broker = Broker()
        brokers.add(broker)

    def delete_broker(self):
        # delete broker 
        pass