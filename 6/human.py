human_0 = {
    'first_name': 'georgiy',
    'last_name': 'starkov',
    'age': 31,
    'current_city': 'SaintPetersburg',
    }
human_1 = {
    'first_name': 'albert',
    'last_name': 'elster',
    'age': 27,
    'current_city': 'SaintPetersburg',
    }
human_2 = {
    'first_name': 'natalia',
    'last_name': 'starkova',
    'age': 56,
    'current_city': 'SaintPetersburg',
    }
people = [human_0, human_1, human_2]

for human in people:
    print(human['first_name']
          + " " + human['last_name']
          + ", " + str(human['age'])
          + " years old, "+ human['current_city'])
