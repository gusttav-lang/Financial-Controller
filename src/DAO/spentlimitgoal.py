from src.dao.spentcategory import SpentCategory


class SpentLimitGoal:
    """
    Defines the goals for each Spent Category. There is a standard goal, used as
    a reference and a goal for each month, which should be defined in the 
    beginning of the month
    """
    def __init__(self):
        self.caterogy = SpentCategory()
        self.amount = 0.0