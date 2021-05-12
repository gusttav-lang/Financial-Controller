from src.dao.assetcategory import AssetCategory


class AssetsInMonth:
    """
    Used to note down all assets that the person has. Can be used to compare
    the difference of the beginning and the end of the month with the spent in
    the month. 
    For now, this information has to be filled manually, since the software is
    not computing the CDI and IPCA indexes.
    """
    def __init__(self):
        self._checked_day = None  # int
        self._category = None  # Asset_Category
        self._value = None # must have the same count as assets

    def set_checked_day(self, value : int) : self._checked_day = value
    def set_category(self, value : AssetCategory()) : self._category = value
    def set_value(self, value : float) : self._value = value

    @property
    def checked_day(self):
        return self._checked_day

    @property
    def category(self):
        return self._category

    @property
    def value(self):
        return self._value