def name(city_name, country_name, population = ''):
    if population:
        data = city_name + ', ' + country_name + ' -population=' + (population)
    else:
        data = city_name + ', ' + country_name

    return data


