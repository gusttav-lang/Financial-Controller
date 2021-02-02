from PySide2.QtWidgets import QWidget, QListWidgetItem
from src.ui.objectivesEditor_ui import Ui_objectivesEditor
from PySide2.QtCore import Qt, QDate
from src.dao.project import Project
from src.dao.objective import Objective


class ObjectivesEditor(QWidget):
    def __init__(self, objectives):
        super().__init__()
        self.ui = Ui_objectivesEditor()
        self.ui.setupUi(self)

        # DAO:
        self.__objectives = objectives

        # load interface and connects:
        self.load_objectives()
        self.make_connects()

        # check if can enable delete button
        self.enable_widgets()

        if (self.ui.lw_objectives_list.count() > 0):
            self.ui.lw_objectives_list.setCurrentRow(-1) # corrects a bug for when there is only 1 item in the list
            self.ui.lw_objectives_list.setCurrentRow(0)

    def enable_widgets(self):
        if (self.ui.lw_objectives_list.count() == 0):
            self.ui.btn_delete.setEnabled(False)
            self.ui.lineEdit_Name.setEnabled(False)
            self.ui.lineEdit_finished_definition.setEnabled(False)
            self.ui.dateEdit_deadline.setEnabled(False)
            self.ui.plainTextEdit_description.setEnabled(False)
        else:            
            self.ui.btn_delete.setEnabled(True)
            self.ui.lineEdit_Name.setEnabled(True)
            self.ui.lineEdit_finished_definition.setEnabled(True)
            self.ui.dateEdit_deadline.setEnabled(True)
            self.ui.plainTextEdit_description.setEnabled(True)

    def make_connects(self):
        self.ui.btn_add.clicked.connect(self.add_objective)
        self.ui.btn_delete.clicked.connect(self.delete_objective)
        self.ui.lw_objectives_list.currentRowChanged.connect(self.row_changed)
        self.ui.lineEdit_Name.textChanged.connect(self.name_changed)
        self.ui.lineEdit_Name.textChanged.connect(lambda x: self.__objectives[self.ui.lw_objectives_list.currentRow()].set_name(x))
        self.ui.lineEdit_finished_definition.textChanged.connect(lambda x: self.__objectives[self.ui.lw_objectives_list.currentRow()].set_finished_definition(x))
        self.ui.dateEdit_deadline.editingFinished.connect(self.deadline_edited)
        self.ui.plainTextEdit_description.textChanged.connect(self.description_changed)

    def name_changed(self, new_text):
        """Updates de lw_objectives ListWidgetItem text"""
        current_row = self.ui.lw_objectives_list.currentRow()
        if (current_row > -1 and current_row < self.ui.lw_objectives_list.count()):
            self.ui.lw_objectives_list.currentItem().setText(new_text)

    def description_changed(self):
        # QPlainTextEdit does not have textChanged. We must do it:
        self.__objectives[self.ui.lw_objectives_list.currentRow()].set_description(self.ui.plainTextEdit_description.toPlainText())

    def deadline_edited(self):
        current_row = self.ui.lw_objectives_list.currentRow()
        if (current_row > -1 and current_row < self.ui.lw_objectives_list.count()):
            self.__objectives[current_row].set_deadline(self.ui.dateEdit_deadline.date().toPython())
    
    def add_list_widget_item(self, objective : Objective):
        item = QListWidgetItem()
        item.setText(objective.name)
        self.ui.lw_objectives_list.addItem(item)
        self.enable_widgets()
        self.ui.lw_objectives_list.setCurrentRow(self.ui.lw_objectives_list.count() - 1)

    def load_objectives(self):
        for objective in self.__objectives:
            self.add_list_widget_item(objective)

    def add_objective(self):
        # add new objective and listwidgetitem
        objective = Objective()
        self.__objectives.append(objective)
        self.add_list_widget_item(objective)
        self.enable_widgets()

    def delete_objective(self):
        # delete objective
        row = self.ui.lw_objectives_list.currentRow()
        if (row > -1 and row < self.ui.lw_objectives_list.count()):
            self.ui.lw_objectives_list.takeItem(row)
            self.__objectives.pop(row)
        self.enable_widgets()

    def row_changed(self, row : int):        
        if (row > -1 and row < self.ui.lw_objectives_list.count()):
            self.ui.lineEdit_Name.setText(self.__objectives[row].name)
            self.ui.lineEdit_finished_definition.setText(self.__objectives[row].finished_definition)
            year = self.__objectives[row].deadline.year
            month = self.__objectives[row].deadline.month
            day = self.__objectives[row].deadline.day
            self.ui.dateEdit_deadline.setDate(QDate(year, month, day))
            self.ui.plainTextEdit_description.setPlainText(self.__objectives[row].description)
