prompt = "Enter the topping to add or enter 'quit' to end additions : "
flag = True

while flag:
	topping = input(prompt)

	if topping == 'quit':
		flag = False
	else:
		print(f"Adding {topping} to the pizza")