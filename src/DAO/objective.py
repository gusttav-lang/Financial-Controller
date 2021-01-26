import datetime

class Objective:
    """
    Represent an objective for the next years. Every asset must have one 
    objective. An objective needs a deadline and a finish definition
    """
    def __init__(self):
        self.name = "New objective"
        self.description = ""
        self.deadline = datetime.date.today()
        self.finished_definition ""