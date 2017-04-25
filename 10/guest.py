full_path = '/Users/jorje_g/git/python_work/10/text_files/guest.txt'
name = input("What is you name: ")
with open(full_path, 'w') as file_object:
    file_object.write(name + "\n")
