alien_color = 'red'

if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
elif alien_color == 'red':
    point = 15

print("You earned " + str(point) + " points.\n")

stage = 32

if stage < 2:
    print("Baby")
elif stage < 4:
    print("toddler")
elif stage < 13:
    print("kid")
elif stage < 20:
    print("teenager")
elif stage < 65:
    print("adult")
elif stage >= 65:
    print("elder")

print('\n')

favorite_fruits = ['banana', 'orange', 'apple']

if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'orange' in favorite_fruits:
    print("You really like oranges!")
if 'pineapple' in favorite_fruits:
    print("You really like pineapples!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'strawberry' in favorite_fruits:
    print("You really like strawberrys!")
