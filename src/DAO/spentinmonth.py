from src.dao.spent import Spent
from src.dao.spentlimitgoal import SpentLimitGoal
from src.dao.fixedspent import FixedSpent
from src.dao.revenueforecast import RevenueForecast
from src.dao.assetsinmonth import AssetsInMonth

class SpentInMonth:
    """
    Class used to store all spent of the month.
    """
    def __init__(self):
        self.month = 1
        self.year = 2021
        self.spent_list = [] # Spent
        self.spent_limit_goal = [] # SpentLimitGoal
        self.fixed_spent = [] # FixedSpent
        self.revenue_forecast = [] # RevenueForecast
        self.assets_in_month = [] # AssetsInMonth