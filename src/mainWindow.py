from PySide2.QtWidgets import QMainWindow, QWidget, QTreeWidgetItem, QFileDialog, QMessageBox
from src.ui.mainWindow_ui import Ui_MainWindow
from PySide2.QtCore import Qt

# DAO:
from src.dao.project import Project
from src.dao.projectdao import ProjectDAO

# Interfaces:
from src.brokersEditor import BrokersEditor
from src.objectivesEditor import ObjectivesEditor

# Definition of strings:
from src.globalvars import GlobalVars as gv


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # UI Setup:
        self.setWindowState(Qt.WindowMaximized)
        self.ui.dw_esquerdo.setTitleBarWidget(QWidget()) # esconder a barra

        # DAO:
        self.__project = None

        self.make_initial_connects()

    def make_initial_connects(self):
        self.ui.actionNovo.triggered.connect(self.new_project)
        self.ui.actionAbrir.triggered.connect(self.open_project)
        self.ui.actionSalvar.triggered.connect(self.save_project)
        self.ui.actionFechar.triggered.connect(self.close_project)
        self.ui.actionSobre.triggered.connect(self.about_software)

    def new_project(self):
        self.__project = Project()
        self.load_interface()

    def open_project(self):
        # TODO: adicionar msg para quando ja existir projeto aberto
        if not ProjectDAO.load_project(file_path, self.__project):
            QMessageBox.critical(self, "Erro", "Arquivo corrompido ou inválido", QMessageBox.Ok)
        
        self.load_interface()
        self.make_connects()

    def save_project(self):
        if isinstance(self.__project, Project):
            file_path, _ = QFileDialog.getSaveFileName(self, "Nome do projeto",
                                                       "",
                                                       "Financial Controller Project (*.fcp)")
            if file_path != "":
                if ProjectDAO.save_project(file_path, self.__project):
                    return True
                else:
                    QMessageBox.critical(self, "Erro", "Caminho inválido", QMessageBox.Ok)
        return False

    def close_project(self):
        self.__project = None

    def about_software(self):
        pass # create new dialog
        
    def load_interface(self):        
        # load tree items:
        tree_item_contas = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_contas.setText(0, gv.corretoras)
        
        tree_item_ativos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_ativos.setText(0, gv.ativos)
        
        tree_item_passivos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_passivos.setText(0, gv.passivos)
                
        tree_item_objetivos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_objetivos.setText(0, gv.objetivos)
        
        tree_item_gastos_fixos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_gastos_fixos.setText(0, gv.gastos_fixos)
        
        tree_item_previsao_receitas = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_previsao_receitas.setText(0, gv.previsao_receitas)
        
        tree_item_teto_gastos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_teto_gastos.setText(0, gv.teto_gastos)
        
        #TODO: colocar isso em outro lugar
        tree_item_categorias = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_categorias.setText(0, gv.categorias)
        
        tree_item_gastos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_gastos.setText(0, gv.gastos)

        self.ui.tw_esquerdo.itemClicked.connect(self.tree_item_clicked)
        
    def tree_item_clicked(self, item):
        if isinstance(item, QTreeWidgetItem):
            # preciso limpar sw_central?
            while (self.ui.sw_central.count() > 0):
                self.ui.sw_central.removeWidget(self.ui.sw_central.widget(0))
            if (item.text(0) == gv.corretoras):
                brokerEdt = BrokersEditor(self.__project.brokers)
                self.ui.sw_central.addWidget(brokerEdt)
                # self.ui.sw_central.setCurrentWidget(brokerEdt) 
                # self.ui.sw_central.setCurrentIndex(0)
            elif (item.text(0) == gv.objetivos):
                objectivesEdt = ObjectivesEditor(self.__project.objectives)
                self.ui.sw_central.addWidget(objectivesEdt)
                