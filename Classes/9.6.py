class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        des = 'Name of the restaurant is: '+self.restaurant_name.title()+'\nType of the cuisine: '+self.cuisine_type.title()
        return des

    def open_restaurant(self):
        open = 'Restaurant is open now. \n'
        return open

restaurant = Restaurant('sabka','non-veg')

class IceCreamStand(Restaurant):
    def __init__(self,cusine_type):
        super().__init__(self, cusine_type)
        self.flavors = ['hbef','diu']

    def show(self):
        print(self.flavors)

ice = IceCreamStand('cusine_type')










class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()

    # def describe_battery(self):
    #     print("This car has a " + str(self.battery_size) + '-kwh battery.')

    def read_odometer(self):
        print('Kuch bhi')


class Battery:
    def __init__(self, battery_size=85):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + '-kwh battery.')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge'
        print(message)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())


# my_tesla.describe_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
