from PySide2.QtWidgets import QMainWindow, QWidget, QTreeWidgetItem, QFileDialog, QMessageBox, QMenu, QAction, QTreeWidgetItemIterator
from src.ui.mainWindow_ui import Ui_MainWindow
from PySide2.QtCore import Qt, QModelIndex

# Tools:
from src.tools.TreeWidgetItemMonthYear import TreeWidgetItemMonthYear
from src.tools.TreeWidgetItemYear import TreeWidgetItemYear

# DAO:
from src.dao.project import Project
from src.dao.projectdao import ProjectDAO
from src.dao.spentinmonth import SpentInMonth
from src.dao.yearpredictions import YearPredictions

# Interfaces:
from src.brokersEditor import BrokersEditor
from src.objectivesEditor import ObjectivesEditor
from src.spentCategoryEditor import SpentCategoryEditor
from src.assetsEditor import AssetsEditor
from src.liabilitiesEditor import LiabilitiesEditor
from src.spentLimitGoalEditor import SpentLimitGoalEditor
from src.spentInMonthEditor import SpentInMonthEditor
from src.addSpentMonth import AddSpentMonth
from src.spenteditor import SpentEditor
from src.spentInYearEditor import SpentInYearEditor

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

        tree_item_categorias_ativos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_categorias_ativos.setText(0, gv.categorias_ativos)
        
        tree_item_ativos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_ativos.setText(0, gv.ativos)
        
        tree_item_passivos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_passivos.setText(0, gv.passivos)
        
        #tree_item_gastos_fixos = QTreeWidgetItem(self.ui.tw_esquerdo)
        #tree_item_gastos_fixos.setText(0, gv.gastos_fixos)
        
        #tree_item_previsao_receitas = QTreeWidgetItem(self.ui.tw_esquerdo)
        #tree_item_previsao_receitas.setText(0, gv.previsao_receitas)
        
        tree_item_categorias_gastos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_categorias_gastos.setText(0, gv.categorias_gastos)

        tree_item_teto_gastos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_teto_gastos.setText(0, gv.teto_gastos)
                
        tree_item_ideal = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_ideal.setText(0, gv.alocacao_ideal)
        
        tree_item_gastos = QTreeWidgetItem(self.ui.tw_esquerdo)
        tree_item_gastos.setText(0, gv.gastos)

        self.ui.tw_esquerdo.itemClicked.connect(self.tree_item_clicked)        

        # add years and months in tree:
        for new_spent in self.__project.spent_in_month:
            self.add_spent_in_tree(new_spent)

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
            new_spent.year = add_interface.selected_year
            new_spent.month = add_interface.selected_month
            self.__project.spent_in_month.append(new_spent)
            self.add_spent_in_tree(new_spent)           

    def add_spent_in_tree(self, new_spent : SpentInMonth):
         # create QTreeWidgetItem:
            tree_item_gastos_list = self.ui.tw_esquerdo.findItems(gv.gastos, Qt.MatchExactly, 0) # get a list of QTreeWidgetItem
            tree_item_year_list = self.ui.tw_esquerdo.findItems(str(new_spent.year), Qt.MatchExactly | Qt.MatchRecursive, 0)
            if (len(tree_item_year_list) == 0):
                if (YearPredictions.is_year_in_list(new_spent.year, self.__project.year_predictions_list) == True):
                    year_predictions = YearPredictions.find_year_in_list(new_spent.year, self.__project.year_predictions_list)
                else:
                    year_predictions = YearPredictions()
                    year_predictions._year = new_spent.year
                self.__project.year_predictions_list.append(year_predictions)
                new_year_item = TreeWidgetItemYear(tree_item_gastos_list[0], year_predictions)
                new_year_item.setText(0, str(new_spent.year))
                tree_item_year_list.append(new_year_item)
            tree_item_new_month = TreeWidgetItemMonthYear(tree_item_year_list[0], new_spent)
            tree_item_new_month.setText(0, gv.Meses[new_spent.month])
            self.sort_tree_months_and_years()
            self.ui.tw_esquerdo.expandAll()
    
    def sort_tree_months_and_years(self):
        #sort the months in ascendend order in the year and sort the years in ascendend order
        tree_item_gastos_list = self.ui.tw_esquerdo.findItems(gv.gastos, Qt.MatchExactly, 0) # get a list of QTreeWidgetItem
        tree_item_gastos_list[0].sortChildren(0, Qt.AscendingOrder)

        # step 1: convert months to int:
        it1 = QTreeWidgetItemIterator(tree_item_gastos_list[0])
        it1 += 1 # start after 'gastos'
        while(it1.value()):
            try:                
                int(it1.value().text(0))
            except ValueError:
                it1.value().setText(0, gv.Meses_Sort_toLetter[it1.value().text(0)])                
            it1 += 1

        # step 2: sort months:
        it2 = QTreeWidgetItemIterator(tree_item_gastos_list[0])
        it2 += 1 # start after 'gastos'
        while(it2.value()):
            try:                
                int(it2.value().text(0))
                it2.value().sortChildren(0, Qt.AscendingOrder)                  
            except ValueError:
                pass # do nothing         
            it2 += 1

        # step 3: convert months bach to str:
        it3 = QTreeWidgetItemIterator(tree_item_gastos_list[0])
        it3 += 1 # start after 'gastos'
        while(it3.value()):
            try:                
                int(it3.value().text(0))
            except ValueError:
                it3.value().setText(0, gv.Meses_Sort_toMonth[it3.value().text(0)])
            it3 += 1

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
            elif (item.text(0) == gv.categorias_gastos):
                spentCategoryEdt = SpentCategoryEditor(self.__project.spent_categories)
                self.ui.sw_central.addWidget(spentCategoryEdt)
            elif (item.text(0) == gv.categorias_ativos):
                assetCategoryEdt = SpentCategoryEditor(self.__project.asset_categories)
                self.ui.sw_central.addWidget(assetCategoryEdt)
            elif (item.text(0) == gv.ativos):
                assetEdt = AssetsEditor(self.__project.assets, self.__project.brokers, self.__project.objectives, self.__project.asset_categories)
                self.ui.sw_central.addWidget(assetEdt)
            elif (item.text(0) == gv.passivos):
                liabilityEdt = LiabilitiesEditor(self.__project.liabilities, self.__project.brokers)
                self.ui.sw_central.addWidget(liabilityEdt)
            elif (item.text(0) == gv.teto_gastos):
                spentLimitEdt = SpentLimitGoalEditor(self.__project.standard_spent_limit, self.__project.spent_categories)
                self.ui.sw_central.addWidget(spentLimitEdt)
            elif (item.text(0) == gv.gastos):
                spentEdt = SpentEditor(self.new_spent_month)
                self.ui.sw_central.addWidget(spentEdt)
            elif (isinstance(item, TreeWidgetItemMonthYear)):
                spentMonthEdt = SpentInMonthEditor(item.spent_in_month, self.__project.spent_categories, self.__project.standard_spent_limit)
                self.ui.sw_central.addWidget(spentMonthEdt)
            elif (isinstance(item, TreeWidgetItemYear)):
                spentYearEdt = SpentInYearEditor(item.year_predictions, self.__project.spent_in_month, self.__project.spent_categories)
                self.ui.sw_central.addWidget(spentYearEdt)
