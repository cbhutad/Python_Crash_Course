class Employee():
    """Models an Employee basic features"""

    def __init__(self,firstname,lastname,annual_sal):
        self.firstname = firstname
        self.lastname = lastname
        self.annual_sal = annual_sal

    def give_raise(self, raiseVal=5000):
        self.annual_sal += int(raiseVal)