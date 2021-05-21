from src.dao.valuesinyear import ValuesInYear


class YearPredictions:
    """
    Used to predict the earnings and spent for the following year
    """
    def __init__(self):
        self._year = None  # Int
        self._earning_list = []  # ValuesInYear
        self._spent_list = []  # ValuesInYear

    @staticmethod
    def is_year_in_list(year: int, ylist):
        '''Used to check if the object for given year has already an instance'''
        for year_precition in ylist:
            if (year == year_precition._year):
                return True
        return False

    @staticmethod
    def find_year_in_list(year: int, ylist):
        """Returns the instance correspending to year in ylist"""
        for year_precition in ylist:
            if (year_precition == year_precition):
                return year_precition
        return None
    