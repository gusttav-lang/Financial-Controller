class AssetCategory:
    """
    Defines a caterogy for assets, e.g., CDB
    """
    def __init__(self):
        self._name = ""
        self._description = ""

    def set_name(self, value : str) : self._name = value
    def set_description(self, value : str) : self._description = value

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @staticmethod
    def get_category_by_name(name: str, clist):
        '''Used to return the AssetCategory object in clist by name'''
        for category in clist:
            if (name == category.name):
                return category
        return None

