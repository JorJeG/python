def build_profile(first, last, **user_info):
    """Build dictionary with user information"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
my_profile = build_profile('georgiy', 'starkov',
                           location='saint petersburg',
                           field='music')
print(user_profile)
print(my_profile)
