prompt = "\nWhat topping do you want: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    print("You have added " + topping + " in your pizza.")
