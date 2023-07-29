import json

def read_fav_num(file):
    num = input("Enter your favorite number : ")
    
    with open(file,"w") as file_obj:
        json.dump(num,file_obj)

    