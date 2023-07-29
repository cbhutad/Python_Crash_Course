""" This program calculates the number of words in the given text file. 
    The exception handling code has also been added.
"""

file = "input_files\odyssey.txt"

try:
    with open(file,encoding="utf-8") as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print(f"The {file} does not exist at the path mentioned")
else:
    words = contents.split(" ")
    print(f"Total words in the {file} : {len(words)}")