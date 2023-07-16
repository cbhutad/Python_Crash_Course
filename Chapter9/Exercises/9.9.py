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

class Battery:

    def __init__(self,battery=75):
        self.battery = battery

    def describe_battery(self):
        print(f"The car has {self.battery}-kWh battery")

    def get_range(self):
        if self.battery == 75:
            range = 140
        elif self.battery > 75:
            range = 200
        else:
            range = 0
        
        print(f"Car can go {range} miles in a single charge")

    def update_battery(self):
        if self.battery != 100:
            self.battery = 100

class ElectricCar(Car):

    def __init__(self,make,model,year):
        super().__init__(make, model, year)
        self.battery = Battery()


tesla = ElectricCar("tesla", "model s", 2019)
print(tesla.get_descriptive_name())
print(tesla.model)
tesla.battery.describe_battery()
tesla.battery.get_range()
tesla.battery.update_battery()
tesla.battery.get_range()