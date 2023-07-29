import json

def output_fav_num(file):

    try:
        with open(file,"r") as file_obj:
            num = json.load(file_obj)
    except FileNotFoundError:
        print(f"{file} does not exist")
    else:
        print(f"Favorite number entered was : {num}")
