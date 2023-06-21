rivers = {
	"nile" : "egypt",
	"ganges" : "india",
	"thames" : "england",
}

for key,value in rivers.items():
	print(f"{key} runs through {value}")

print()

for key in rivers.keys():
	print(f"{key} is a river")

print()

for value in rivers.values():
	print(f"{value} is a country")


