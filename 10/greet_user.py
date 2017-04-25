import json

def get_stored_username():
    """Request a stored username"""
    filename = '/Users/jorje_g/git/python_work/10/text_files/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Request a new username"""
    filename = '/Users/jorje_g/git/python_work/10/text_files/username.json'
    username = input("What is your name: ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greeting user by name"""
    username = get_stored_username()
    if username:
        while True:
            print(username.title() + ". Is it your name?")
            answer = input("(y/n)")
            if answer == 'y':
                print("Welcome back " + username.title())
                break
            elif answer == 'n':
                username = get_new_username()
                break
            else:
                print("Please, type 'y' or 'n'")
    else:
        username = get_new_username()


greet_user()
