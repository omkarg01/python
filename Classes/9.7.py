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


class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

    # def show_privileges(self):
    #     string = ['can add post', 'can delete post', 'can ban user']
    #     for i in string:
    #         print(i)

class Privileges():
    def __init__(self):
        pass

    def show_privileges(self):
        string = ['can add post', 'can delete post', 'can ban user']
        for i in string:
            print(i)

ad = Admin('omkar', 'gujja','ifne')

ad.privileges.show_privileges()

