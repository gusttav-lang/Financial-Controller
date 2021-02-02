class SpentCategory:
    """
    Defines a caterogy for spent, e.g., food
    """
    def __init__(self):
        self._name = "New Category"
        self._description = ""

    def set_name(self, value : str) : self._name = value
    def set_description(self, value : str) : self._description = value

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description
