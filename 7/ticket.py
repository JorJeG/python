prompt = "\nHow old are you: "
active = 2

while active > 0:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("You can see this film for free.")
    elif age < 12:
        print("You can see this film  for $10.")
    elif age >= 12:
        print("You can see this film for $15.")
    active -= 1
