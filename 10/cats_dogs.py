filename_cats = '/Users/jorje_g/git/python_work/10/text_files/cats.txt'
filename_dogs = '/Users/jorje_g/git/python_work/10/text_files/dogs.txt'

def print_names(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
        #msg = 'Sorry, the file ' + filename + " does not exist."
        #print(msg)
    else:
        print(contents.rstrip() + '\n')


print_names(filename_cats)
print_names(filename_dogs)
