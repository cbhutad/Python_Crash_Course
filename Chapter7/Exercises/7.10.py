responses = {}

polling_active = True

while polling_active:

	name = input("Enter your name : ")
	destination = input("Where you would like to visit : ")

	responses[name] = destination

	repeat = input("Would anyone else want to continue : (yes/no)")
	if repeat == "no":
		polling_active = False

print("Polling results are : ")
for name,destination in responses.items():
	print(f"{name} would like to visit {destination}")