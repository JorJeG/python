def show_magicians(names):
    for name in names:
        print(name.title())

def make_great(magicians, great_magicians):
    while magicians:
        current_magician = magicians.pop()
        current_magician = "Great " + current_magician
        great_magicians.append(current_magician)
magicians = ['alice', 'david', 'carolina']
great_magicians = []
make_great(magicians[:], great_magicians)
show_magicians(great_magicians)
show_magicians(magicians)
