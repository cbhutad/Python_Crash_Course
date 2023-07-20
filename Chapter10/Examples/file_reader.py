# Reading entire contents of a file. Gives a extra blank string in output. This is quirk for the read() function but not being displayed for this python version.

#filename = "pi_digits.txt"
#filename = "input_files/pi_digits.txt" -> relative path
filename = "D:\\Python_Crash_Course\\Chapter10\\Examples\\input_files\\pi_digits.txt" # Absolute path

with open(filename) as file_object:
    contents = file_object.read()

#print(contents)
print(contents.rstrip(),end="")

print()
# Reading file content using read() but dealing with lines. Here the \n will be printed and print adds it own new line character at the end. So we removed them using the rstrip function

filename2 = "pi_digits.txt"

with open(filename2) as file_object:
    for line in file_object:
        print(line.rstrip())


