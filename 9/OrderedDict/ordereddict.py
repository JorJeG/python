from collections import OrderedDict

knowed_words = OrderedDict()
knowed_words['list'] = "Allow to store sets of information in one place"
knowed_words['dictionary'] = "Allow to connect pieces of related information."
knowed_words['function'] = "It is named blocks of code."
knowed_words['class'] = "Classes that represent real-world things and situations"

for word, description in knowed_words.items():
    print(word.title() + ": " + description)
