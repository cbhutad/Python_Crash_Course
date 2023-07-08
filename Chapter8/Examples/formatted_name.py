# Simple function returning a value

# def get_formatted_name(first_name, last_name):
#     """Return a full name, nicely formatted"""
#     fullname = f"{first_name} {last_name}"
#     return fullname.title()

# musician = get_formatted_name(last_name="Hendrix", first_name="Jimi")
# print(musician)

# Modifiying above function to accept optional values

def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, nicely formatted"""
    if middle_name != "":
        fullname = f"{first_name} {middle_name} {last_name}"
    else:
        fullname = f"{first_name} {last_name}"

    return fullname.title()

musician = get_formatted_name(first_name="Joy", last_name="Hooker", middle_name="Lee")
print(musician)

musician = get_formatted_name(first_name="Jimi", last_name="Hendrix")
print(musician)

