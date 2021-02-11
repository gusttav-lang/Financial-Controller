from src.dao.spentcategory import SpentCategory


class SpentLimitGoal:
    """
    Defines the goals for each Spent Category. There is a standard goal, used as
    a reference and a goal for each month, which should be defined in the 
    beginning of the month
    """
    def __init__(self):
        self._category = SpentCategory()
        self._amount = 0.0

    def set_category(self, value : SpentCategory) : self._category = value
    def set_amount(self, value : float) : self._amount = value

    @property
    def category(self):
        return self._category

    @property
    def amount(self):
        return self._amount