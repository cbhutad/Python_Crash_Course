# reading the content as list of lines

filename = "pi_digits.txt"

with open(filename) as file_object:
    contents = file_object.readlines()

pi_string = ""
for line in contents:
    pi_string += line.strip() # this will remove the \n charactes in the content but the spaces before the 2nd and 3rd line still will be displayed

print(pi_string) # returns the pi digits as string output.