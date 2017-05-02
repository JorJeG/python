import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for class Employee"""

    def setUp(self):
        """Create instance of employee and his increase to salary"""
        self.anton = Employee('Anton', 'Chehov', 5000)

    def test_give_default_raise(self):
        self.anton.get_raise()

        self.assertEqual(10000, self.anton.a_salary)

    def test_give_custom_raise(self):
        self.anton.get_raise(12000)

        self.assertEqual(17000, self.anton.a_salary)


unittest.main()
