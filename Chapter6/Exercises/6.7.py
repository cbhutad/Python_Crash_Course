person1 = {
	"first_name" : "Cheenmaya",
	"last_name" : "Bhutad",
	"age" : 26,
	"city" : "Chandrapur"
}

person2 = {
	"first_name" : "Abhijit",
	"last_name" : "K S",
	"age" : 26,
	"city" : "Kochi"
}

people = [person1, person2]

for person in people:
	print(f"Details for {person.get('first_name')} are : ")
	print(f"\t Full Name : {person.get('first_name')} {person.get('last_name')}")
	print(f"\t Age : {person.get('age')}")
	print(f"\t City : {person.get('city')}")
	print()