# Working as a greeter

def get_formatted_name(first_name, last_name):
    """Return a full name, nicely formatted"""
    fullname = f"{first_name} {last_name}"
    return fullname.title()

while True:

    first = input("Your first name please : ")
    last = input("Your second name please : ")

    fullname = get_formatted_name(last_name=last, first_name=first)
    print(f"Welcome, {fullname}")

    guests_remaining = input("Are there anymore guests : enter yes or no ")
    if guests_remaining.lower() == "no":
        break

