class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"We are {self.restaurant_name}.")
        print(f"we specialize in {self.cuisine_type}")

    def open_restaurant(self):
        print("We are Open for business")