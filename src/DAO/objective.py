import datetime

class Objective:
    """
    Represent an objective for the next years. Every asset must have one 
    objective. An objective needs a deadline and a finish definition
    """
    def __init__(self):
        self._name = "New objective"
        self._description = ""
        self._deadline = datetime.date.today()
        self._finished_definition = ""

    def set_name(self, value : str) : self._name = value
    def set_description(self, value : str) : self._description = value
    def set_deadline(self, value : datetime.date) : self._deadline = value
    def set_finished_definition(self, value : str) : self._finished_definition = value

    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description

    @property
    def deadline(self):
        return self._deadline

    @property
    def finished_definition(self):
        return self._finished_definition
