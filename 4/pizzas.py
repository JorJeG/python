pizzas = ['pepperoni', 'cheese', 'tomato']
friend_pizzas = pizzas[:]

pizzas.append('saliami')
friend_pizzas.append('bekon')

print("My favorite pizzas are:")
for pizza in pizzas:
    print("I like " + pizza + " pizza.")

print("I really love pizza!")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("I like " + pizza + " pizza.")

print("My friend really love pizza!")
