larsi = {
    'kind': 'cat',
    'owner': 'georgiy',
    }
marzipan = {
    'kind': 'dog',
    'owner': 'ivan',
    }
vilveta = {
    'kind': 'cat',
    'owner': 'yulia',
    }

pets = [larsi, marzipan, vilveta]

for pet in pets:
    print(pet['owner'] + " have a " + pet['kind'])
