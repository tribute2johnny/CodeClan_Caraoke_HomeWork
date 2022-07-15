import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        
        self.room_1 = Room("Room 1")
        self.room_2 = Room("Room 2")
        self.room_3 = Room("Room 3")

    def test_room_has_number(self):
        self.assertEqual("Room 1", self.room_1.room_number)

    def test_song_list_starts_at_0(self):
        self.assertEqual(0, self.room_1.song_count())

    def test_can_add_song_to_room(self):
        self.room_1.add_song(self.room_1)
        self.assertEqual(1, self.room_1.song_count())

    def test_room_starts_empty(self):
        self.assertEqual(0, self.room_2.guest_count())

    def test_can_check_in_guest_to_room(self):
        guest = Guest("David", 24)
        self.room_2.check_in(guest)
        self.assertEqual(1, self.room_2.guest_count())

    def test_can_remove_guest_from_room(self):
        guest = Guest("David", 24)
        self.room_2.check_in(guest)
        self.room_2.check_out(guest)
        self.assertEqual(0, self.room_2.guest_count())
