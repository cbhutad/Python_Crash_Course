# using function to greet a list of users

def greet_users(names):

    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

users = ["hannah", "ty", "margot"]
greet_users(users)