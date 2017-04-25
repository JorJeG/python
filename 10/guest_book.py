full_path = '/Users/jorje_g/git/python_work/10/text_files/guest_book.txt'
while True:
    prompt = 'What is your name: \n'
    prompt += '(Enter "q" for exit) '
    name = input(prompt)
    if name == 'q':
        break
    else:
        print("Welcome " + name.title())
        with open(full_path, 'a') as file_object:
            file_object.write(name + '\n')
