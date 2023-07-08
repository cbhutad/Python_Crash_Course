# Notes

### Parameters and Arguments

- If we have a parameters with default values then they must be placed after non default parameters else we receive a syntax error `python-verison : 3.11.0`. This is observed even in the case that we call the functions using keyword arguments

``` Python

def describe_pets(animal_type = "dog", pet_name):
    """Display information about pet"""
    print(f"I have a {animal_type}")
    print(f"My {animal_type} name is {pet_name.title()}")

describe_pets(pet_name="Harry")

```
Here we will receive a Syntax error.

