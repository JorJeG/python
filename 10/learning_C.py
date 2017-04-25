full_path = '/Users/jorje_g/git/python_work/10/text_files/learning_python.txt'
with open(full_path) as file_object:
    lines = file_object.readlines()
full_file = ''
for line in lines:
    line = line.replace('Python', 'C')
    full_file += line
print(full_file)
