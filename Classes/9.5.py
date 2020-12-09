class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        des = ('First name: ' + self.first_name + '\nLast name: ' + self.last_name)
        return des.title()

    def greet_user(self):
        gre = 'Hello ' + self.first_name + '!, How are you?\n '
        return gre.title()

    def show(self):
        print(self.login_attempts)

    def increment_login_attempt(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User('omkar', 'gujja')
#user_1.reset_login_attempts()

user_1.increment_login_attempt()
user_1.increment_login_attempt()
user_1.increment_login_attempt()
user_1.increment_login_attempt()
user_1.increment_login_attempt()

#user_1.reset_login_attempts()


user_1.show()

