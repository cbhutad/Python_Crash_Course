filename = "input_files/Chapter_Topics.txt"

# with open(filename) as file_obj1:
#     contents = file_obj1.read()
#     print(contents)

with open(filename) as file_obj:
    contents = file_obj.readlines()

for line in contents:
    print(line.rstrip())
        

