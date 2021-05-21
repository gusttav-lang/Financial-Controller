class ValuesInYear:
    """
    Defines what is a value used to predict the year earnings and spent
    """
    def __init__(self):
        self._how_much = None # float
        self._where = ""
        self._parcels = None # int

    def set_where(self, value : str) : self._where = value
    def set_how_much(self, value : float) : self._how_much = value
    def set_parcels(self, value : int) : self._parcels = value
    
    @property
    def where(self):
        return self._where
    
    @property
    def how_much(self):
        return self._how_much
        
    @property
    def parcels(self):
        return self._parcels
