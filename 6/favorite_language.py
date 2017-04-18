favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah']
# or for name in favorite_languages
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("  Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!\n")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
