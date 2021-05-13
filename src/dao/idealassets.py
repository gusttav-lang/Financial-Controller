from src.dao.assetcategory import AssetCategory


class IdealAssets:
    """Class used to define the ideal proportion between assets"""
    def __init__(self):
        self._category = AssetCategory()  # AssetCategory
        self._min_value = None  # float
        self._ideal_value = None  # float
        self._max_value = None  # float

    def set_category(self, value : AssetCategory) : self._category = value
    def set_min_value(self, value : float) :        
        try:
            fl = float(value)
        except:
            fl = None        
        self._min_value = fl
    def set_ideal_value(self, value : float) :        
        try:
            fl = float(value)
        except:
            fl = None        
        self._ideal_value = fl
    def set_max_value(self, value : float) :        
        try:
            fl = float(value)
        except:
            fl = None        
        self._max_value = fl

    @property
    def category(self):
        return self._category

    @property
    def min_value(self):
        return self._min_value

    @property
    def ideal_value(self):
        return self._ideal_value

    @property
    def max_value(self):
        return self._max_value
        