def open_restaurant():
    open = 'Restaurant is open now. \n'
    return open


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        des = 'Name of the restaurant is: ' + self.restaurant_name.title() + '\nType of the cuisine: ' + self.cuisine_type.title()
        return des


restaurant = Restaurant('sabka', 'non-veg')
hotels = Restaurant('jfnjfe', 'bjbdbwd')

print(restaurant.describe_restaurant())
print(open_restaurant())

print(hotels.describe_restaurant())
print(open_restaurant())


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        des = ('First name: ' + self.first_name + '\nLast name: ' + self.last_name)
        return des.title()

    def greet_user(self):
        gre = 'Hello ' + self.first_name + '!, How are you?\n '
        return gre.title()


user_1 = User('omkar', 'gujja')

print(user_1.describe_user())
print(user_1.greet_user())


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        d = self.name + ' is now sitting.'
        return d.title()

    def roll_over(self):
        ro = self.name + ' rolled over! '
        return ro.title()


my_dog = Dog('willie', 5)

print('My dog name is ' + my_dog.name + '.')
print('My dog is ' + str(my_dog.age) + '.')
