pet1 = {
	"type" : "labrador",
	"owner" : "owner1"
}

pet2 = {
	"type" : "bulldog",
	"owner" : "owner2"
}


pet3 = {
	"type" : "german shepherd",
	"owner" : "owner3"
}


pet4 = {
	"type" : "doberman",
	"owner" : "owner4"
}

pet5 = {
	"type" : "corgi",
	"owner" : "owner5"
}

pets = [pet1,pet2,pet3,pet4,pet5]

for pet in pets:
	print(f"Pet details are : ")
	print(f"\t Type : {pet.get('type')}")
	print(f"\t Owner : {pet.get('owner')}")
	print()