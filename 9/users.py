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


aeinstein = User('albert', 'einstein', 76, 'male')
aeinstein.describe_user()
aeinstein.greet_user()

gstarkov = User('georg', 'starkov', 31, 'male')
gstarkov.increment_login_attempts()
gstarkov.increment_login_attempts()
gstarkov.increment_login_attempts()
print(gstarkov.login_attempts)
gstarkov.reset_login_attempts()
print(gstarkov.login_attempts)
