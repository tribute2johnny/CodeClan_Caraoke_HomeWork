import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("David", 24)
        self.guest_2 = Guest("Laura", 26)
        self.guest_3 = Guest("Tamara", 30)
        self.guest_4 = Guest("Fraser", 28)

    def test_guest_has_name(self):
        self.assertEqual("David", self.guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(28, self.guest_4.age)