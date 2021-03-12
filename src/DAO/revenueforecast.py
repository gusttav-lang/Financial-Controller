from src.dao.recurringvalues import  RecurringValues


class RevenueForecast(RecurringValues):
    """
    Represents the Revenue which should occur every month, e.g., wage
    """
    def __init__(self):
        super().__init__()