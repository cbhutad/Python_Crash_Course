import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        """Set up a employee object and provide test data required"""
        self.new_emp = Employee("cheenmaya", "bhutad", 50000)
        self.default_raise_sal = 55000
        self.custom_raise_sal = 60000

    def test_give_raise_defaultcase(self):
        self.new_emp.give_raise()
        self.assertEqual(self.default_raise_sal, self.new_emp.annual_sal)

    def test_give_raise_customraise(self):
        self.new_emp.give_raise(10000)
        self.assertEqual(self.custom_raise_sal, self.new_emp.annual_sal) 


if __name__ == "__main__":
    unittest.main()