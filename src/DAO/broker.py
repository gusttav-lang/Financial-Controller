class Broker():
    """
    Represents a broker or bank, where the assets are stored
    """
    def __init__(self):
        self.__name = "New broker"
        self.__bank_number = 0

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def bank_number(self):
        return __bank_number
    
    @bank_number.setter
    def bank_number(self, value):
        __bank_number = value