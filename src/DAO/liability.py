import datetime
from src.dao.broker import Broker


class Liability:
    """
    Represents a liability.
    """
    def __init__(self):
        self._name = "New liability"
        self._broker = Broker()
        self._purchase_day = datetime.date.today()
        self._expiration_day = datetime.date.today()
        self._interest = "100% CDI" # it is a string since CDI and IPCA values are not defined in the software
        self._borrowed_money = 1000.0

    def set_name(self, value : str) : self._name = value
    def set_broker(self, value : Broker) : self._broker = value
    def set_purchase_day(self, value : datetime.date) : self._purchase_day = value
    def set_expiration_day(self, value : datetime.date) : self._expiration_day = value
    def set_interest(self, value : str) : self._interest = value
    def set_borrowed_money(self, value : float) : self._borrowed_money = value

    @property
    def name(self):
        return self._name
    
    @property
    def broker(self):
        return self._broker

    @property
    def purchase_day(self):
        return self._purchase_day

    @property
    def expiration_day(self):
        return self._expiration_day

    @property
    def interest(self):
        return self._interest

    @property
    def borrowed_money(self):
        return self._borrowed_money
