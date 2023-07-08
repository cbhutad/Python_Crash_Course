def store_car_info(manufacturer, model, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info

car_details = store_car_info("subaru", "outback", color="blue", tow_packages=True)
print(car_details)