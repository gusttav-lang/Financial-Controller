import datetime
from src.dao.objective import Objective
from src.dao.broker import Broker


class Asset:
    """
    Represents an asset.
    """
    def __init__(self):
        self.name = "New asset"
        self.broker = Broker()
        self.purchase_day = datetime.date.today()
        self.expiration_day = datetime.date.today()
        self.interest = "100% CDI" # it is a string since CDI and IPCA values are not defined in the software
        self.applied_money = 1000.0
        self.objective = Objective()