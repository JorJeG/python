from restaurant import Restaurant

restaurant = Restaurant('red fox', 'pub')
restaurant2 = Restaurant('jimi hendrix', 'club')
restaurant3 = Restaurant('jagger', 'club')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.open_restaurant()
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant.set_number_served(16)
print(restaurant.number_served)
restaurant.increment_number_served(24)
print(restaurant.number_served)
