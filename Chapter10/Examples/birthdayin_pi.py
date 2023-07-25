filename = "input_files/pi_million_digits.txt"

with open(filename) as file_object:
    content = file_object.readlines()

pi_string = ""
for line in content:
    pi_string += line.strip()

birthday = input("Enter birthdate in yymmdd format : \n")

if birthday in pi_string:
    print("Your birthdate is present in the million pi_digits")
else:
    print("Better luck next time")