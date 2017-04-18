favorite_places = {
    'georgiy': [
                'saint petersburg',
                'london',
                'cremea',
                ],
    'natalia': [
                'saint petersburg',
                'pechora',
                'ural mountains',
                ],
    'vasiliy': [
                'bruges',
                'praha',
                'budapest',
                ],
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())
