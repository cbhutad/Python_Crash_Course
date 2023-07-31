def city_country(city, country, population=""):
    """Returns the city, country format string in a capitalized format"""

    if population != "":
        return f"{city.title()}, {country.title()} - population {population}"
    return f"{city}, {country}".title()