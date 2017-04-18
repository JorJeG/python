cities = {
    'saint petersburg': {
        'country': 'russia',
        'population': '7m',
        'fact': 'FC Zenith',
        },
    'milan': {
        'country': 'italia',
        'population': '5m',
        'fact': 'FC Arsenal',
        },
    'london': {
        'country': 'UK',
        'population': '8m',
        'fact': 'A.C. Milan',
        },
    }

for city, city_info in sorted(cities.items()):
    print("\nCity: " + city.title())
    print("\tCountry: " + city_info['country'].title())
    print("\tPopulation: " + city_info['population'])
    print("\tFact: " + city_info['fact'])
