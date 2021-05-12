from src.dao.spentcategory import SpentCategory
import datetime


class Spent:
    """
    Defines a spent. It must have the spent day, amount, place and category
    """
    def __init__(self):
        self._day = None # datetime.date.today()
        self._how_much = None # float
        self._where = ""
        self._category = None # SpentCategory()

    def set_where(self, value : str) : self._where = value
    def set_how_much(self, value : float) :
        try:
            fl = float(value)
        except:
            fl = None
        self._how_much = fl
    def set_day(self, day: int, month: int, year: int) : 
        try:
            value = datetime.date(year, month, int(day))
        except:
            value = None
        self._day = value
    def set_category(self, value : SpentCategory) : self._category = value
    
    @property
    def where(self):
        return self._where
    
    @property
    def how_much(self):
        return self._how_much
    
    @property
    def day_in_month(self):
        if (self._day == None) : return None 
        return self._day.day
        
    @property
    def category(self):
        return self._category
