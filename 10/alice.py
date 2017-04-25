full_path = '/Users/jorje_g/git/python_work/10/text_files/alice.txt'

try:
    with open(full_path) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + full_path + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + full_path + " has about "
          + str(num_words) + " words.")
