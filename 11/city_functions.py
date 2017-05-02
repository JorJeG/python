def get_formatted_info(city, country, population=''):
    """Formate city and country info"""
    if population:
        overall = city + ", " + country + " - " + str(population)
    else:
        overall = city + ", " + country
    return overall.title()
