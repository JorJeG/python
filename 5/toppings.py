#               ЗАКАЗАННЫЕ ДОПОЛНЕНИЯ к пицце
#requested_toppings = ['mushrooms', 'onions', 'pineapple']

#if 'mushrooms' in requested_toppings:
#    print("Adding mushrooms.")
#if 'pepperoni' in requested_toppings:
#    print("Adding pepperoni")
#if 'pepperoni' not in requested_toppings:
#    print("Not adding pepperoni")

#print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers']

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'fresh fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
