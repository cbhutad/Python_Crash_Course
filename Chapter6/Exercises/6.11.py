cities = {
	"delhi" : {
		"fact" : "capital of 3 states",
		"location" : "India",
	},
	"tokyo" : {
		"fact" : "called land of rising sun",
		"location" : "Japan",
	},
	"new-york" : {
		"fact" : "Most boring city of world",
		"location" : "USA",
	}
}

for city,info in cities.items():
	print(f"Information about {city} : ")
	print(f"\tfact : {info.get('fact')}")
	print(f"\tlocation : {info.get('location')}")
	print()
