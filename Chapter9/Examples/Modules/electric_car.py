from car import Car

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

class ElectricCar(Car):

    def __init__(self,make,model,year):
        super().__init__(make, model, year)
        self.battery = Battery()