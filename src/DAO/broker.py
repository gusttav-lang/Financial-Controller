class Broker:
    """
    Represents a broker or bank, where the assets are stored
    """
    def __init__(self):
        self.__name = "New broker"
        self.__bank_number = 0
        self.__description = "Describe for what is used"

    @property
    def name(self):
        return self.__name

    @property
    def bank_number(self):
        return self.__bank_number

    @property
    def description(self):
        return self.__description
      
    def set_name(self, value):
        self.__name = value

    def set_description(self, value : str):
        self.__description = value

    def set_bank_number(self, value : int):
        try:
            self.__bank_number = int(value)
        except:
            raise TypeError("Only Integers are allowed")