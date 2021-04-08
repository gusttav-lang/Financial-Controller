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
        self._checked_day = 0  # int
        self._assets = []  # Asset_Category
        self._values = [] # must have the same count as assets

    def set_checked_day(self, value : str) : self._name = value

    @property
    def checked_day(self):
        return self._checked_day