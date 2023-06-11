name1 = "\tcheenmaya bhutad\t"
name2 = "\ncheenmaya bhutad\n"
name3 = " cheenmaya bhutad "

print("Without strip API : \n")

print(name1)
print(name2)
print(name3)

print("\n")

print("With lstrip : \n")

print(name1.lstrip())
print(name2.lstrip())
print(name3.lstrip())

print("\n")

print("With rstrip : \n")

print(name1.rstrip())
print(name2.rstrip())
print(name3.rstrip())

print("\n")

print("With strip : \n")

print(name1.strip())
print(name2.strip())
print(name3.strip())

print("\n")