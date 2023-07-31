import unittest
from name_formatter import get_formatted_name

class Test_Name_Formatter(unittest.TestCase):
    """Test case for name_formatter.py"""

    def test_first_last_combo(self):
        formatted_name = get_formatted_name("abhijit", "ks")
        self.assertEqual(formatted_name, "Abhijit Ks")

    def test_first_middle_last_combo(self):
        formatted_name = get_formatted_name("Cheenmaya", "Bhutad", "Rajendra")
        self.assertEqual(formatted_name, "Cheenmaya Rajendra Bhutad")

if __name__ == "__main__":
    unittest.main()
