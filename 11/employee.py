class Employee():
    """"""

    def __init__(self, f_name, l_name, a_salary):
        self.f_name = f_name
        self.l_name = l_name
        self.a_salary = a_salary

    def get_raise(self, increase=5000):
        """Increase salary"""
        self.a_salary += increase
