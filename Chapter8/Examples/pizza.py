# using variable arguments in a function

# def make_pizza(*toppings):

#     print("Making a pizza with toppings : ")
#     for topping in toppings:
#         print(f"{topping}")

# make_pizza("mushrooms", "green peppers", "extra cheese")

# using positional and variable arguments mix in a function

def make_pizza(size, *toppings):
    print(f"Making a pizza of size {size} with toppings:")
    for topping in toppings:
        print(f"{topping}")

make_pizza("large", "mushrooms", "green peppers", "extra cheese")

