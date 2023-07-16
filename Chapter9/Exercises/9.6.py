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
    
class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ["Mango", "Choclate", "Vanilla", "Butterscotch"]

    def display_flavors(self):
        print("We have this flavors of icecream : ")
        for flavor in self.flavors:
            print(f"\t {flavor}")

bhari_ice_cream = IceCreamStand("bhari_ice_cream", "scones")
bhari_ice_cream.display_flavors()
