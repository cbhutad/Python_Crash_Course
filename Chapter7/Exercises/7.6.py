# Using the conditional test in while condition

# prompt = "Enter your age for ticket price or enter -1 to quit : "

# age = int(input(prompt))

# while age != -1: 

# 	if age < 3:
# 		print("Costs 0 rupees")
# 	elif age >= 3  and age < 12 :
# 		print("Costs 10 rupees")
# 	elif age >= 12:
# 		print("Costs 15 rupees")

# 	age = int(input(prompt))

# # Using the break statement to get out of while loop

prompt = "Enter your age for ticket price or enter -1 to quit : "

while True: 

	age = int(input(prompt))

	if age == -1:
		break
	elif age < 3:
		print("Costs 0 rupees")
	elif age >= 3  and age < 12 :
		print("Costs 10 rupees")
	elif age >= 12:
		print("Costs 15 rupees")