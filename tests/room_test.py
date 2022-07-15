import unittest

from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(1)
        self.room_2 = Room(2)
        self.room_3 = Room(3)

    def test_room_has_number(self):
        self.assertEqual(1, self.room_1.room_number)

    def room_starts_empty(self):
        self.assertEqual(0,)
    