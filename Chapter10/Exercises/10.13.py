import json

file = "output_files\\username.json"

def get_stored_username(file):
    """Get stored username if avaialable"""
    try:
        with open(file,"r") as file_obj:
            username = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(file):
    """Prompt for a new username"""
    username = input("Enter your name : ")
    with open(file,"w") as file_obj:
        json.dump(username,file_obj)
    
def greet_user():
    username = get_stored_username(file)
    if username:
        print(f"Is this the correct username : {username}")
        choice = input("enter yes or no : ")
        if choice.lower() == "yes":
            print(f"Welcome back {username}")
        else:
            get_new_username(file)
    else:
        get_new_username(file)

greet_user()
greet_user()