"""module for 9.12 exercise"""
from user import User

class Privileges:

    def __init__(self):
        self.privileges = ["add post", "update post", "delete post"]
    
    def show_privileges(self):
        print("Admin can do the following : ")
        for permission in self.privileges:
            print(f"\t {permission}")

class Admin(User):
    
    def __init__(self,first_name,last_name,age,gender):
        super().__init__(first_name,last_name,age,gender)
        self.privileges = Privileges()