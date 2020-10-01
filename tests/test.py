import unittest
from location import ApiLocation

class TestMathFunctions(unittest.TestCase):
    def test_get_location(self):
        check_ip = ApiLocation.get_ip(self)
        self.assertEqual(type(check_ip), str)
        self.assertIsNotNone(check_ip)






print("check")




