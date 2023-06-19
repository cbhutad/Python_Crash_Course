my_foods = ["pizza", "falafel", "carrot cake"]
my_foods_copy = my_foods[:]


my_foods_copy.append("pani puri")
my_foods.append("ice cream")

for food in my_foods:
	print(food,end=" ")

print()

for food in my_foods_copy:
	print(food,end=" ")
