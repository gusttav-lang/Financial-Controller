from dao.stockcriteria import StockCriteria
from src.dao.broker import Broker
from src.dao.asset import Asset
from src.dao.liability import Liability
from src.dao.objective import Objective
from src.dao.spentcategory import SpentCategory
from src.dao.spentinmonth import  SpentInMonth
from src.dao.spentlimitgoal import SpentLimitGoal
from src.dao.stockcriteria import StockCriteria
from src.dao.emergencyreserveforidealassets import EmergencyReserveForIdealAssets


class Project:
    """
    The project gathers all information of a person.
    """
    def __init__(self):
        self.brokers = [] # Broker
        self.assets = [] # Asset
        self.liabilities = [] # Liability
        self.objectives = [] # Objective
        self.spent_categories = [] # SpentCategory
        self.spent_in_month = [] # SpentInMonth
        self.standard_spent_limit = [] # SpentLimitGoal
        self.asset_categories = [] # AssetCategory
        self.year_predictions_list = [] # YearPredicitons
        self.assets_in_dates_list = []  # AssetsInMonth - used in Ideal Assets Editor
        self.ideal_assets_list = []  # Ideal Assets
        self.stock_criteria = StockCriteria()
        self.emergency_reserver_for_ideal_assets = EmergencyReserveForIdealAssets()
