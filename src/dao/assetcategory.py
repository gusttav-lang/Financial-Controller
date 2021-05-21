class AssetCategory:
    """
    Defines a caterogy for assets, e.g., CDB
    """
    def __init__(self):
        self._name = "New Category"
        self._description = ""
        self._opportunity_definition = ""

    def set_name(self, value : str) : self._name = value
    def set_description(self, value : str) : self._description = value
    def set_opportunity_definition(self, value : str) : self._opportunity_definition = value

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def opportunity_definition(self):
        return self._opportunity_definition

    @staticmethod
    def get_category_by_name(name: str, clist):
        '''Used to return the AssetCategory object in clist by name'''
        for category in clist:
            if (name == category.name):
                return category
        return None

