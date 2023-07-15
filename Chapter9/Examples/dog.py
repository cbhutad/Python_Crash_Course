# Example for a simple class

class Dog:
    """Simple attempt to model a Dog"""

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name} siiitt")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog("Willie",6)
print(f" My dog is {my_dog.age} old")
my_dog.sit()
my_dog.roll_over()