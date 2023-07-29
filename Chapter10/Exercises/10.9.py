file1 = "input_files\cat.txt"
file2 = "input_files\dogs.txt"

def file_processing(filename):
    try:
        with open(file,"r") as file_obj:
            contents = file_obj.readlines()
    except FileNotFoundError:
        #print(f"given {filename} does not exist at the path")
        pass
    else:
        for line in contents:
            print(line.strip())
        print()

for file in [file1,file2]:
    file_processing(file)