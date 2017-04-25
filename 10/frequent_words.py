filepath = '/Users/jorje_g/git/python_work/10/text_files/An_English_Girl_in_Japan.txt'

with open(filepath) as f_obj:
    contents = f_obj.read()
    count = contents.lower().count('the')
    print(count)
