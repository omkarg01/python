import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('omkar', 'gujja')
        self.assertEqual(formatted_name, 'Omkar Gujja')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('omkar', 'gujja', 'sudarshan')
        self.assertEqual(formatted_name, 'Omkar Sudarshan Gujja')

if __name__ == '__main__':
    unittest.name()
