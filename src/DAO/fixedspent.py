from src.dao.recurringvalues import RecurringValues
from src.dao.spentcategory import SpentCategory


class FixedSpent(RecurringValues):
    """
    Represents the spent which occur every month, e.g., electricity bill
    """
    def __init__(self):
        super().__init__()
        self._category = None # SpentCategory

    def set_category(self, value : SpentCategory) : self._category = value
    
    @property
    def category(self):
        return self._category