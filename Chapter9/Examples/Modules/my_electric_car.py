from electric_car import ElectricCar

tesla = ElectricCar("tesla", "model s", 2019)
print(tesla.get_descriptive_name())
tesla.battery.describe_battery()
tesla.battery.get_range()