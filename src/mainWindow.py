from PySide2.QtWidgets import QMainWindow, QWidget, QTreeWidgetItem, QFileDialog, QMessageBox, QMenu, QAction
from src.ui.mainWindow_ui import Ui_MainWindow
from PySide2.QtCore import Qt, QModelIndex

# DAO:
from src.dao.project import Project
from src.dao.projectdao import ProjectDAO
from src.dao.spentinmonth import SpentInMonth

# Interfaces:
from src.brokersEditor import BrokersEditor
from src.objectivesEditor import ObjectivesEditor
from src.spentCategoryEditor import SpentCategoryEditor
from src.assetsEditor import AssetsEditor
from src.liabilitiesEditor import LiabilitiesEditor
from src.spentLimitGoalEditor import SpentLimitGoalEditor
from src.spentInMonthEditor import SpentInMonthEditor
from src.addSpentMonth import AddSpentMonth

# Definition of strings:
from src.globalvars import GlobalVars as gv


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # UI Setup:
        #self.setWindowState(Qt.WindowMaximized)
        self.ui.dw_esquerdo.setTitleBarWidget(QWidget()) # esconder a barra

        #Internal vars:
        self.menu_add_delete_father = None
        self.act_new_spent = None
        self.act_delete_spent = None

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
        self.__project = Project()
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select File', '', 'Financial Controller Project (*.fcp)')
        if not ProjectDAO.load_project(file_path, self.__project):
            QMessageBox.critical(self, "Erro", "Arquivo corrompido ou inválido", QMessageBox.Ok)
            return
        self.load_interface()

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
        while (self.ui.tw_esquerdo.topLevelItemCount() > 0):
            self.ui.tw_esquerdo.takeTopLevelItem(0)
        while (self.ui.sw_central.count() > 0):
            self.ui.sw_central.removeWidget(self.ui.sw_central.widget(0))

    def about_software(self):
        pass # create new dialog
        
    def load_interface(self):        
        # load tree items:
        tree_item_contas = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_contas.setText(0, gv.corretoras)
                
        tree_item_objetivos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_objetivos.setText(0, gv.objetivos)
        
        tree_item_ativos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_ativos.setText(0, gv.ativos)
        
        tree_item_passivos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_passivos.setText(0, gv.passivos)
        
        #tree_item_gastos_fixos = QTreeWidgetItem(self.ui.tw_esquerdo)
        #tree_item_gastos_fixos.setText(0, gv.gastos_fixos)
        
        #tree_item_previsao_receitas = QTreeWidgetItem(self.ui.tw_esquerdo)
        #tree_item_previsao_receitas.setText(0, gv.previsao_receitas)
        
        tree_item_categorias = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_categorias.setText(0, gv.categorias)

        tree_item_teto_gastos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_teto_gastos.setText(0, gv.teto_gastos)
                
        tree_item_ideal = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_ideal.setText(0, gv.alocacao_ideal)
        
        tree_item_gastos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_gastos.setText(0, gv.gastos)

        self.ui.tw_esquerdo.itemClicked.connect(self.tree_item_clicked)

        #menus creation:
        self.menu_add_delete_father = QMenu(self.ui.tw_esquerdo) # used to group new and delete
        self.act_new_spent = QAction("Adicionar novo mês")
        self.act_delete_spent = QAction("Deletar mês")
        self.act_new_spent.triggered.connect(self.new_spent_month)
        self.act_delete_spent.triggered.connect(self.delete_spent_month)
        self.menu_add_delete_father.addAction(self.act_new_spent)
        self.menu_add_delete_father.addAction(self.act_delete_spent)
        self.ui.tw_esquerdo.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tw_esquerdo.customContextMenuRequested.connect(self.menu_tw_esquerdo)

    def menu_tw_esquerdo(self, pos):
        model_index = self.ui.tw_esquerdo.indexAt(pos) # QModelIndex()
        if (model_index.isValid()):
            if(self.ui.tw_esquerdo.currentItem().text(0) == gv.gastos):
                self.act_delete_spent.setEnabled(False)
                self.act_new_spent.setEnabled(True)
                self.menu_add_delete_father.popup(self.ui.tw_esquerdo.viewport().mapToGlobal(pos))
            if(self.ui.tw_esquerdo.currentItem().parent() != None):
                if(self.ui.tw_esquerdo.currentItem().parent().text(0) == gv.gastos):
                    self.act_delete_spent.setEnabled(True)
                    self.act_new_spent.setEnabled(True)
                    self.menu_add_delete_father.popup(self.ui.tw_esquerdo.viewport().mapToGlobal(pos))
        
    
    def new_spent_month(self):
        add_interface = AddSpentMonth(self.__project.spent_in_month)
        add_interface.exec()

        if add_interface.confirmed:
            # create object:
            new_spent = SpentInMonth()
            self.__project.spent_in_month.append(new_spent)
            new_spent.year = add_interface.selected_year
            new_spent.month = add_interface.selected_month

            # create QTreeWidgetItem:
            tree_item_gastos_list = self.ui.tw_esquerdo.findItems(gv.gastos, Qt.MatchExactly, 0) # get a list of QTreeWidgetItem
            tree_item_year_list = self.ui.tw_esquerdo.findItems(str(add_interface.selected_year), Qt.MatchExactly | Qt.MatchRecursive, 0) # parei aqui, nao ta funcionando
            if (len(tree_item_year_list) == 0):
                new_year_item = QTreeWidgetItem(tree_item_gastos_list[0])
                new_year_item.setText(0, str(add_interface.selected_year))
                tree_item_year_list.append(new_year_item)
            tree_item_new_month = QTreeWidgetItem(tree_item_year_list[0])
            #tree_item_new_month.setText(0, str(add_interface.selected_month))
            tree_item_new_month.setText(0, gv.Meses[add_interface.selected_month])
            self.update_tree_months_in_year()
            self.ui.tw_esquerdo.expandAll()

    def update_tree_months_in_year(self):
        #sort in the months in ascendend order
        pass

    def delete_spent_month(self):
        #remove da lista e apaga treewidgetitem
        pass
        
    def tree_item_clicked(self, item):
        if isinstance(item, QTreeWidgetItem):
            # preciso limpar sw_central?
            while (self.ui.sw_central.count() > 0):
                self.ui.sw_central.removeWidget(self.ui.sw_central.widget(0))
            if (item.text(0) == gv.corretoras):
                brokerEdt = BrokersEditor(self.__project.brokers)
                self.ui.sw_central.addWidget(brokerEdt)
            elif (item.text(0) == gv.objetivos):
                objectivesEdt = ObjectivesEditor(self.__project.objectives)
                self.ui.sw_central.addWidget(objectivesEdt)
            elif (item.text(0) == gv.categorias):
                spentCategoryEdt = SpentCategoryEditor(self.__project.spent_categories)
                self.ui.sw_central.addWidget(spentCategoryEdt)
            elif (item.text(0) == gv.ativos):
                assetEdt = AssetsEditor(self.__project.assets, self.__project.brokers, self.__project.objectives)
                self.ui.sw_central.addWidget(assetEdt)
            elif (item.text(0) == gv.passivos):
                liabilityEdt = LiabilitiesEditor(self.__project.liabilities, self.__project.brokers)
                self.ui.sw_central.addWidget(liabilityEdt)
            elif (item.text(0) == gv.teto_gastos):
                spentLimitEdt = SpentLimitGoalEditor(self.__project.standard_spent_limit, self.__project.spent_categories)
                self.ui.sw_central.addWidget(spentLimitEdt)
            elif (item.text(0) == gv.gastos):
                #spentEdt = SpentInMonthEditor() adicionar alguma tela generica que permita adicionar um mês novo e que tenha resumo do que já está cadastrado
                pass
