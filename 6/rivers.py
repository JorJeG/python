rivers = {
    'nile': 'egypt',
    'volga': 'russia',
    'mississippi': 'usa',
    }
for river, country in rivers.items():
    print("The " + river.title() +
          " runs throught " + country.title())
for river in rivers.keys():
    print(river.title())
print()
for country in rivers.values():
    print(country.title())
