responses = {}
active = True

while active:
    name = input("\nWhat is your name? ")
    response = input("Where do you want to spend a holiday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        active = False

print("\n--- Results ---")
for name, response in responses.items():
    print(name.title() + " likes to spend a holiday in " + response.title())
