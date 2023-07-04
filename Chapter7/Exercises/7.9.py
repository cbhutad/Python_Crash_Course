sandwich_orders = ["chicken tandoori", "pastrami", "pastrami","corn cheese", "choclate", "cheese grilled"]

print("We are out of pastrami")

while "pastrami" in sandwich_orders:
	sandwich_orders.remove("pastrami")

print(sandwich_orders)