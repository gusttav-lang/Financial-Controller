from src.dao.broker import Broker
from src.dao.asset import Asset
from src.dao.liability import Liability
from src.dao.objective import Objective
from src.dao.spentcategory import SpentCategory
from src.dao.spentinmonth import  SpentInMonth
from src.dao.spentlimitgoal import SpentLimitGoal


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