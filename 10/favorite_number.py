import json


def get_stored_number():
    """Request a number if it was saved"""
    filename = '/Users/jorje_g/git/python_work/10/text_files/favorite_number.json'
    try:
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def get_new_number():
    """Request a new favorite number and save"""
    favorite_number = input("What is your favorite number: ")
    filename = '/Users/jorje_g/git/python_work/10/text_files/favorite_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
        return favorite_number

def fav_number():
    favorite_number = get_stored_number()
    if favorite_number:
        print("Your favorite number is " + favorite_number)
    else:
        favorite_number = get_new_number()

fav_number()
