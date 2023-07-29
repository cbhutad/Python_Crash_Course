import json

file = "output_files\\number.json"

def read_fav_num(file):
    try:
        with open(file,"r") as file_obj:
            num = json.load(file_obj)
    except FileNotFoundError:
        return None 
    else:
        return num

def store_fav_num(file):
    num = input("Enter favorite number : ")
    with open(file,"w") as file_obj:
        json.dump(num,file_obj)
    
def fav_num():
    num = read_fav_num(file)
    if num:
        print(f"Favorite number is {num}")
    else:
        store_fav_num(file)

fav_num()
fav_num()