from PySide2.QtWidgets import QMainWindow, QWidget, QTreeWidgetItem
from src.ui.mainWindow_ui import Ui_MainWindow
from PySide2.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      
        
        self.load_interface()
        
    def load_interface(self):
        self.setWindowState(Qt.WindowMaximized)
        self.ui.dw_esquerdo.setTitleBarWidget(QWidget()) # esconder a barra
        
        #load tree items:
        tree_item_contas = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_contas.setText(0, "Corretoras")
        
        tree_item_ativos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_ativos.setText(0, "Ativos")
        
        tree_item_passivos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_passivos.setText(0, "Passivos")
                
        tree_item_objetivos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_objetivos.setText(0, "Objetivos")
        
        tree_item_previsoes = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_previsoes.setText(0, "Valores recorrentes")
        
        tree_item_gastos_fixos = QTreeWidgetItem(tree_item_previsoes)
        tree_item_gastos_fixos.setText(0, "Gastos fixos")
        
        tree_item_previsao_receitas = QTreeWidgetItem(tree_item_previsoes)
        tree_item_previsao_receitas.setText(0, "Previsão de receitas")
        
        tree_item_teto_gastos = QTreeWidgetItem(tree_item_previsoes)
        tree_item_teto_gastos.setText(0, "Teto de gastos")
        
        #TODO: colocar isso em outro lugar
        tree_item_categorias = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_categorias.setText(0, "Categorias")
        
        tree_item_gastos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_gastos.setText(0, "Gastos")
        