def city_country(city,country):
    if country == 'usa':
        a = '"' + city.title() + ', ' + country.upper() + '"'
    else:
        a = '"'+city.title()+', '+country.title()+'"'
    return a

print(city_country('mumbai','india'))
print(city_country('new york','usa'))
print(city_country('tokyo','japan'))
