print("enter 2 numbers to add")
print("enter q to quit")

while True:
    num1 = input("Enter first number : ")
    if num1 == "q":
        break
    num2 = input("Enter second number : ")
    if num2 == "q":
        break
    try:
        result = int(num1) + int(num2)
    except ValueError:
        print("Number cannot be in text format")
    else:
        print(f"Sum is {result}")
