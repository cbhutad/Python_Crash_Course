numbers = {
	"user1" : list(range(1,6)),
	"user2" : list(range(1,11)),
}

for user,numberLists in numbers.items():
	print(f"List of numbers liked by {user} are : ")
	print("\t",end="")
	for number in numberLists:
		print(f"{number}",end=" ")
	print()