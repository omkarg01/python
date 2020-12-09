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
    def __init__(self, battery_size=70):
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

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()

my_tesla.battery.get_range()



