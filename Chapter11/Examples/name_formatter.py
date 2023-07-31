def get_formatted_name(first, last, middle=""):
    """Returns a formatted name in capitalized format"""

    if middle != "":
        return f"{first} {middle} {last}".title()
    return f"{first} {last}".title()