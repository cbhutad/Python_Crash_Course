sandwich_orders = ["chicken tandoori", "corn cheese", "choclate", "cheese grilled"]
finished_sandwiches = list()

while len(sandwich_orders) > 0:
	sandwich = sandwich_orders.pop(0)
	print(f"{sandwich} ready")
	finished_sandwiches.append(sandwich)

print("Today's orders : ")
for sandwich in finished_sandwiches:
	print(sandwich.title())