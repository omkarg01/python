def open_restaurant():
    open = 'Restaurant is open now. \n'
    return open


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 25

    def describe_restaurant(self):
        des = 'Name of the restaurant is: ' + self.restaurant_name.title() + '\nType of the cuisine: ' + self.cuisine_type.title() + '\nNo. of served: ' + str(
            self.number_served)
        return des

    def set_number_served(self, increased):
        if increased > self.number_served:
            print('not possible')

            # self.number_served = increased
        else:
            # print('not possible')
            self.number_served = increased

    def increment_number_served(self, number):
        self.number_served += number



restaurant = Restaurant('sabka', 'non-veg')
# restaurant.number_served = 25

#print(restaurant.set_number_served(15))
restaurant.increment_number_served(25)

print(restaurant.describe_restaurant())

#restaurant.increment_number_served(25)
