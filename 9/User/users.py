from user import User
from admin import Admin

new_admin = Admin('stepan', 'safronov', 23, 'male')
new_admin.privileges.show_privileges()
