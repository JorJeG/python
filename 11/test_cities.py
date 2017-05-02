import unittest
from city_functions import get_formatted_info

class InfoTestCase(unittest.TestCase):
    """Test for 'city_functions.py'"""

    def test_city_country(self):
        """Correct print 'Santiago, Chile'"""

        formatted_output = get_formatted_info('santiago', 'chile')
        self.assertEqual(formatted_output, 'Santiago, Chile')

    def test_city_country_population(self):
        """Correct print 'Santiago, Chile - 5000000'"""
        formatted_output = get_formatted_info('santiago', 'chile', 5000000)
        self.assertEqual(formatted_output, 'Santiago, Chile - 5000000')


unittest.main()
