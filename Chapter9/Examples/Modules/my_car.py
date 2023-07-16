from car import Car

car1 = Car("audi", "R4", 2019)
print(car1.get_descriptive_name())

car1.odometer_reading = 23
car1.read_odometer()