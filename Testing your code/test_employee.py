import unittest
from detail_info import Employee

class EmployeeIncrement(unittest.TestCase):
    def setUp(self):
        self.employee_name = Employee('harry', 'dsouza', 65000)

    def default_raise(self):
        self.employee_name.give_raise()
        # b = f'${self.employee_name.annual_salary + self.employee_name.give_raise()}: is your new incremented annual salary.'
        # self.assertEqual(b, give_raise())
        b = '$70000: is your new incremented annual salary.'
        self.assertEqual(self.employee_name.give_raise(), b)

    def test_give_custom_raise(self):
        self.employee_name.give_raise(12000)
        # c = f'${self.employee_name.annual_salary + self.employee_name.give_raise(12000)}: is your new incremented annual salary.'
        # self.assertEqual(c, give_raise(12000))
        c = '$77000: is your new incremented annual salary.'
        self.assertEqual(self.employee_name.give_raise(12000), c)




if __name__ == '__main__':
    unittest.main()