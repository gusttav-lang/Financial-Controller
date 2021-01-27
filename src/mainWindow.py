from PySide2.QtWidgets import QMainWindow, QWidget, QTreeWidgetItem, QFileDialog, QMessageBox
from src.ui.mainWindow_ui import Ui_MainWindow
from PySide2.QtCore import Qt
from src.dao.project import Project
from src.dao.projectdao import ProjectDAO


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # DAO:
        self.__project = None
        
        self.load_interface()
        self.make_connects()

    def make_connects(self):
        self.ui.actionNovo.triggered.connect(self.new_project)
        self.ui.actionAbrir.triggered.connect(self.open_project)
        self.ui.actionSalvar.triggered.connect(self.save_project)
        self.ui.actionFechar.triggered.connect(self.close_project)
        self.ui.actionSobre.triggered.connect(self.about_software)

    def new_project(self):
        self.__project = Project()

    def open_project(self):
        # TODO: adicionar msg para quando ja existir projeto aberto
        if not ProjectDAO.load_project(file_path, self.__project):
            QMessageBox.critical(self, "Erro", "Arquivo corrompido ou inválido", QMessageBox.Ok)

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
        pass
        
    def load_interface(self):
        self.setWindowState(Qt.WindowMaximized)
        self.ui.dw_esquerdo.setTitleBarWidget(QWidget()) # esconder a barra
        
        # load tree items:
        tree_item_contas = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_contas.setText(0, "Corretoras")
        
        tree_item_ativos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_ativos.setText(0, "Ativos")
        
        tree_item_passivos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_passivos.setText(0, "Passivos")
                
        tree_item_objetivos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_objetivos.setText(0, "Objetivos")
        
        tree_item_gastos_fixos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_gastos_fixos.setText(0, "Gastos fixos")
        
        tree_item_previsao_receitas = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_previsao_receitas.setText(0, "Previsão de receitas")
        
        tree_item_teto_gastos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_teto_gastos.setText(0, "Teto de gastos")
        
        #TODO: colocar isso em outro lugar
        tree_item_categorias = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_categorias.setText(0, "Categorias")
        
        tree_item_gastos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_gastos.setText(0, "Gastos")
        