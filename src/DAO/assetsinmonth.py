import datetime
from src.dao.asset import Asset


class AssetsInMonth:
    """
    Used to note down all assets that the person has. Can be used to compare
    the difference of the beginning and the end of the month with the spent in
    the month. 
    For now, this information has to be filled manually, since the software is
    not computing the CDI and IPCA indexes.
    """
    def __init__(self):
        self.checked_day = datetime.date.today()
        self.assets = []
        self.values = [] # must have the same count as assets