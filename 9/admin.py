class User(object):
    """Simple user class"""

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        fullname = self.first_name + " " + self.last_name
        print(
            fullname.title() + ", "
            + self.sex + ", "
            + str(self.age) + " years old")

    def greet_user(self):
        print("Welcome " + self.first_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges():
    def __init__(self):
        self.privileges = [
            'allowed to add message',
            'allowed to delete user',
            'allowed to ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age, sex):
        super(Admin, self).__init__(first_name, last_name, age, sex)
        self.privileges = Privileges()
        #self.privileges = [
        #    'allowed to add message',
        #    'allowed to delete user',
        #    'allowed to ban user']

    #def show_privileges(self):
    #    for privilege in self.privileges:
    #        print(privilege)


stepan_admin = Admin('stepan', 'safronov', 33, 'male')
stepan_admin.privileges.show_privileges()
