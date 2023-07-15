class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant():
        print(f"We are {self.restaurant_name}.")
        print(f"we specialize in {self.cuisine_type}")

    def open_restaurant(self):
        print("We are Open for business")

restaurant1 = Restaurant("Aroma Hydrebadi House", "Biryani")
restaurant2 = Restaurant("Iya", "Korean")
restaurant3 = Restaurant("Barbecue Nation", "barbecue")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()