# Storing the values in a dictionary and return this dictionary

# def build_person(first_name, last_name):
#     """Return a dictionary with information about the person"""
#     person = {
#         "first" : first_name,
#         "last" : last_name
#     }

#     return person

# musician = build_person(last_name="hendrix", first_name="jimi")

# print(musician)

# Storing a optional parameter if provided as argument in dictionary for the above case

def build_person(first_name, last_name, age=None):
    """Return a dictionary with information about the person"""
    person = {
        "first" : first_name,
        "last" : last_name,
    }

    if age != None:
        person["age"] = age

    return person

musician = build_person(last_name="bhutad", first_name="cheenmaya", age=26)
print(musician)

musician = build_person(last_name="bhutad", first_name="mugdha")
print(musician)