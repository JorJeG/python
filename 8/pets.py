
def describe_pet(animal_type, pet_name):
    """Print information about an animal"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# Positional arguments
#describe_pet('hamster', 'harry')


# Keyword arguments
describe_pet(pet_name='harry', animal_type='hamster')
