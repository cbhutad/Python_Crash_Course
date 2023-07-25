filename = "input_files/Chapter_Topics.txt"

with open(filename) as file_obj:
    contents = file_obj.read()
    print(contents.replace("python","Java"))