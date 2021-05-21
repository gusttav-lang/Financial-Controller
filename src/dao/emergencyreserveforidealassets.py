class EmergencyReserveForIdealAssets:
    """Class stores the current and ideal value for emergency reserve. Used in IdealAssetsEditor.
       Ideally, the current value should be a table. However, it might take some time to implement it"""
    def __init__(self) -> None:
        self._ideal_value = None
        self._current_value = None

    def set_ideal_value(self, value : float) :        
        try:
            fl = float(value)
        except:
            fl = None        
        self._ideal_value = fl
    def set_current_value(self, value : float) :        
        try:
            fl = float(value)
        except:
            fl = None        
        self._current_value = fl

    @property
    def ideal_value(self):
        return self._ideal_value

    @property
    def current_value(self):
        return self._current_value