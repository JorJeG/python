full_path = '/Users/jorje_g/git/python_work/10/text_files/learning_python.txt'
#with open(full_path) as file_object:
#    full_file = file_object.read()
#    print(full_file.strip())

with open(full_path) as file_object:
    lines = file_object.readlines()
file_lines = ''
for line in lines:
    file_lines += line

print(file_lines)
