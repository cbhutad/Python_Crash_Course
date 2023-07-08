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

### Arbitary number of arguments

Whenever a variable arguments are being provided the other type of arguments we can use are positional arguments. In such cases keyword arguments are note allowed.

``` Python

def make_pizza(size, *toppings):
    print(f"Making a pizza of size {size} with toppings:")
    for topping in toppings:
        print(f"{topping}")

make_pizza(size="large", "mushrooms", "green peppers", "extra cheese") # this leads to error

```