class StockCriteria:
    """Class used to register the criterias that the user consider before buying a stock"""
    def __init__(self) -> None:
        self._number_and_sectors = ""
        self._indicators = ""
        self._investor_analysis = ""
        self._valuation = ""
        self._more_criteria = ""