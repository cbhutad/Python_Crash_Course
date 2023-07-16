"""Module for 9.12 exercise"""

class User:

    def __init__(self,first_name,last_name,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print("Details about user : ")
        print(f"\t First name : {self.first_name}")
        print(f"\t Last name : {self.last_name}")
        print(f"\t Age : {self.age}")
        print(f"\t Gender : {self.gender}")
    
    def greet_user(self):
        print(f"Personalized greeting for you : {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0