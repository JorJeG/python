number_places = input("How much seats do you want to book a table: ")
number_places = int(number_places)

if number_places > 8:
    print("\nYou need to wait a little")
else:
    print("\nYour table is ready")
