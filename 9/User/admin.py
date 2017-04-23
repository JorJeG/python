from user import User

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
