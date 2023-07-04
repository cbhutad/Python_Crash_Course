responses = {}

polling_active = True

while polling_active:

	name = input("Enter your name : ")
	response = input("Which mountain you would like to climb : ")

	responses[name] = response

	repeat = input("Would you like to another person to poll (yes/no) : ")
	if repeat == "no":
		polling_active = False

print("Result of polls are : ")

for key,value in responses.items():
	print(f"{key} wants to climb {value}")