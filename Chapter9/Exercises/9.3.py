class User:

    def __init__(self,first_name,last_name,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print("Details about user : ")
        print(f"\t First name : {self.first_name}")
        print(f"\t Last name : {self.last_name}")
        print(f"\t Age : {self.age}")
        print(f"\t Gender : {self.gender}")
    
    def greet_user(self):
        print(f"Personalized greeting for you : {self.first_name} {self.last_name}")

user1 = User("Divyansh", "Raina", 26, "male")
user2 = User("Abhijit", "KS", 26, "male")
user3 = User("Aaditya", "Darade", 23, "male")

user1.describe_user()
user1.greet_user()

print()

user2.describe_user()
user2.greet_user()

print()

user3.describe_user()
user3.greet_user()
