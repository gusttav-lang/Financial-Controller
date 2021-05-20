from PySide2.QtWidgets import QWidget
from src.ui.stockCriteriaEditor_ui import Ui_stockCriteriaEditor
from src.dao.stockcriteria import StockCriteria


class StockCriteriaEditor(QWidget):
    def __init__(self, stock_criteria: StockCriteria):
        super().__init__()
        self.ui = Ui_stockCriteriaEditor()
        self.ui.setupUi(self)

        # DAO:
        self.__stock_criteria = stock_criteria

        # load interface and connects:
        self.load_plain_texts()
        self.make_connects()

    def load_plain_texts(self):
        self.ui.plainTextEdit_number.setPlainText(self.__stock_criteria._number_and_sectors)
        self.ui.plainTextEdit_indicators.setPlainText(self.__stock_criteria._indicators)
        self.ui.plainTextEdit_analysis.setPlainText(self.__stock_criteria._investor_analysis)
        self.ui.plainTextEdit_valuation.setPlainText(self.__stock_criteria._valuation)
        self.ui.plainTextEdit_more_criteria.setPlainText(self.__stock_criteria._more_criteria)

    def make_connects(self):
        self.ui.plainTextEdit_number.textChanged.connect(self.number_changed)
        self.ui.plainTextEdit_indicators.textChanged.connect(self.indicators_changed)
        self.ui.plainTextEdit_analysis.textChanged.connect(self.analysis_changed)
        self.ui.plainTextEdit_valuation.textChanged.connect(self.valuation_changed)
        self.ui.plainTextEdit_more_criteria.textChanged.connect(self.more_criteria_changed)

    def number_changed(self):
        self.__stock_criteria._number_and_sectors = self.ui.plainTextEdit_number.toPlainText()

    def indicators_changed(self):
        self.__stock_criteria._indicators = self.ui.plainTextEdit_indicators.toPlainText()

    def analysis_changed(self):
        self.__stock_criteria._investor_analysis = self.ui.plainTextEdit_analysis.toPlainText()

    def valuation_changed(self):
        self.__stock_criteria._valuation = self.ui.plainTextEdit_valuation.toPlainText()

    def more_criteria_changed(self):
        self.__stock_criteria._more_criteria = self.ui.plainTextEdit_more_criteria.toPlainText()
    