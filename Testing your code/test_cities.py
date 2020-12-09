import unittest
from city_function import name

class CityTest(unittest.TestCase):
    def test_city_country(self):
        format = name('mumbai','india')
        self.assertEqual(format, 'mumbai, india')

    def test_city_country_population(self):
        format = name('mumbai', 'india', '135crore')
        self.assertEqual(format, 'mumbai, india -population=135crore')


unittest.main()

