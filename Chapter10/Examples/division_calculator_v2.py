# without exception handling

# print("Enter the 2 numbers to divided")
# print("Enter q to quit")

# while True:
#     num1 = input("Enter first number : ")
#     if num1 == "q":
#         break
#     num2 = input("Enter second number : ")
#     if  num2 == "q":
#         break
#     quotient = int(num1) / int(num2) # This will cause exception if num2 is zero
#     print(quotient)

# With exception handling

print("Enter the 2 numbers to divided")
print("Enter q to quit")

while True:
    num1 = input("Enter first number : ")
    if num1 == "q":
        break
    num2 = input("Enter second number : ")
    if  num2 == "q":
        break
    try:
        quotient = int(num1) / int(num2) # This will cause exception if num2 is zero
    except ZeroDivisionError:
        print("num2 cannot be zero")
    else:
        print(quotient)

