class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"We are {self.restaurant_name}.")
        print(f"we specialize in {self.cuisine_type}")

    def open_restaurant(self):
        print("We are Open for business")

restaurant1 = Restaurant("restro bar","italian")
#print(restaurant1.restaurant_name)
#print(restaurant1.cuisine_type)
restaurant1.describe_restaurant()
#print(restaurant1.open_restaurant())