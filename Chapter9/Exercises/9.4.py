class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"We are {self.restaurant_name}.")
        print(f"we specialize in {self.cuisine_type}")

    def open_restaurant(self):
        print("We are Open for business")

    def set_number_served(self,numbers):
        self.number_served = numbers

    def increment_number_served(self,numbers):
        if numbers < 0:
            print("Enter valid value")
        else:
            self.number_served += numbers

restaurant1 = Restaurant("Relax, Pure veg", "Vegetaerian")
print(f"Number served : {restaurant1.number_served}")
restaurant1.number_served = 5
print(f"Number served : {restaurant1.number_served}")
restaurant1.set_number_served(10)
print(f"Number served : {restaurant1.number_served}")
restaurant1.increment_number_served(20)
print(f"Number served : {restaurant1.number_served}")
