prompt = "Enter your age for ticket price or enter -1 to quit : "
flag = True

while flag:
	age = int(input(prompt))

	if age == -1:
		flag = False
	elif age < 3:
		print("Costs 0 rupees")
	elif age >= 3  and age < 12 :
		print("Costs 10 rupees")
	elif age >= 12:
		print("Costs 15 rupees")