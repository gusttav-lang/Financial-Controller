from src.dao.spentcategory import SpentCategory
import datetime


class Spent:
    """
    Defines a spent. It must have the spent day, amount, place and category
    """
    def __init__(self):
        self.day = datetime.date.today()
        self.how_much = 0.0
        self.where = ""
        self.category = SpentCategory()