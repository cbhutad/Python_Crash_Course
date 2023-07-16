""" A class that can be used to represent a petrol/diesel and electric car """

class Car:

    def __init__(self,make,model,year):
        """Initialize attributes for instances"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a descriptive name"""
        long_name = f"{self.model} {self.make} {self.year}"
        return long_name.title()

    def read_odometer(self):
        """prints the odometer reading"""
        print(f"The car has {self.odometer_reading} miles on it")

    def update_odometer(self,mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll the odometer back")

    def increment_odometer(self,miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("Miles entered are invalid")