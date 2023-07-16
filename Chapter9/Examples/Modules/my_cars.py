# from car import Car
# from electric_car import ElectricCar

# petrol_car = Car("Audi", "R4", 2019)
# print(petrol_car.get_descriptive_name())

# electric_car = ElectricCar("tesla", "model S", 2019)
# print(electric_car.get_descriptive_name())

# or we can do this below as well

import car
import electric_car

petrol_car = car.Car("Audi", "R4", 2019)
print(petrol_car.get_descriptive_name())

electric_car = electric_car.ElectricCar("tesla", "model S", 2019)
print(electric_car.get_descriptive_name())

