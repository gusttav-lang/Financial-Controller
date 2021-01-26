import datetime
from src.dao.broker import Broker


class Liability:
    """
    Represents a liability.
    """
    def __init__(self):
        self.name = "New liability"
        self.broker = Broker()
        self.purchase_day = datetime.date.today()
        self.expiration_day = datetime.date.today()
        self.interest = "100% CDI" # it is a string since CDI and IPCA values are not defined in the software
        self.borrowed_money = 1000.0