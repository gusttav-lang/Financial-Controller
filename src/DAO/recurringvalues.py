class RecurringValues:
    """
    Abstract class. Used to store the values which occur every month
    """
    def __init__(self):
        self._what = ""
        self._how_much = None # float
        self._day_in_month = None # int

    def set_what(self, value : str) : self._what = value
    def set_how_much(self, value : float) : self._how_much = value
    def set_day_in_month(self, value : int) : self._day_in_month = value
    
    @property
    def what(self):
        return self._what
    
    @property
    def how_much(self):
        return self._how_much
    
    @property
    def day_in_month(self):
        return self._day_in_month
    