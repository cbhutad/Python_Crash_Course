import unittest
from city_functions import city_country

class Test_City_Functions(unittest.TestCase):
    """Test case for city_functions.py module"""

    def test_city_country(self):
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")

    def test_city_country_population(self):
        result = city_country("santiago", "chile", 500000)
        self.assertEqual(result, "Santiago, Chile - population 500000")

if __name__ == "__main__":
    unittest.main()