# Simple function

# def describe_pets():
#     """Display information about a pet"""
#     print("This is info about a function")

# describe_pets()

# Function using positional arguments

# def describe_pets(animal_type, pet_name):
#     """Display information about pet"""
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type} name is {pet_name.title()}")

# describe_pets("Hamster","Harry")

# Function using keyword arguments

# def describe_pets(animal_type,pet_name):
#     """Display information about pet"""
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type} name is {pet_name.title()}")

# describe_pets(pet_name="Harry", animal_type="Hamster")

# Function with default values for parameters

def describe_pets(pet_name, animal_type = "dog"):
    """Display information about pet"""
    print(f"I have a {animal_type}")
    print(f"My {animal_type} name is {pet_name.title()}")

describe_pets(animal_type="Hamster", pet_name="Harry")
