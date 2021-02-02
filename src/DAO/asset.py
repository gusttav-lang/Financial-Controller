import datetime
from src.dao.objective import Objective
from src.dao.broker import Broker


class Asset:
    """
    Represents an asset.
    """
    def __init__(self):
        self._name = "New asset"
        self._broker = None # Broker()
        self._purchase_day = datetime.date.today()
        self._expiration_day = datetime.date.today()
        self._interest = "100% CDI" # it is a string since CDI and IPCA values are not defined in the software
        self._applied_money = 1000.0
        self._objective = None # Objective()

    def set_name(self, value : str) : self._name = value
    def set_broker(self, value : Broker) : self._broker = value
    def set_purchase_day(self, value : datetime.date) : self._purchase_day = value
    def set_expiration_day(self, value : datetime.date) : self._expiration_day = value
    def set_interest(self, value : str) : self._interest = value
    def set_applied_money(self, value : float) : self._applied_money = value
    def set_objective(self, value : Objective) : self._objective = value

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
    def applied_money(self):
        return self._applied_money

    @property
    def objective(self):
        return self._objective
