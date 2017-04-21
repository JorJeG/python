def build_car(type_car, model_car, **car_info):
    car_dict = {}
    car_dict['type'] = type_car
    car_dict['model'] = model_car
    for key, value in car_info.items():
        car_dict[key] = value
    return car_dict


new_car = build_car('subaru', 'outback',
                     color='blue',
                     tow_package=True)
print(new_car)
