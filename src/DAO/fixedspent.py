from src.dao.recurringvalues import RecurringValues
from src.dao.spentcategory import SpentCategory


class FixedSpent(RecurringValues):
    """
    Represents the spent which occur every month, e.g., electricity bill
    """
    def __init__(self):
        self.category = SpentCategory()