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

    def test_can_check_in_and_check_out_guest(self):
        guest = Guest("David", 24)
        self.room_2.check_in(guest)
        self.room_2.check_out(guest)
        self.assertEqual(0, self.room_2.guest_count())

    def test_room_capacity_reached(self):
        guest_1 = Guest("David", 24)
        guest_2 = Guest("Sarah", 26)
        guest_3 = Guest("Tom", 22)
        self.room_2.check_in(guest_1)
        self.room_2.check_in(guest_2)
        self.room_2.check_in(guest_3)
        self.assertEqual("capacity reached", self.room_2.capacity())

    def test_room_has_space(self):
        guest_1 = Guest("David", 24)
        guest_2 = Guest("Sarah", 26)
        self.room_3.check_in(guest_1)
        self.room_3.check_in(guest_2)
        self.assertEqual("room has space", self.room_3.capacity())

    def test_room_cannot_go_over_capacity(self):
        guest_1 = Guest("David", 24)
        guest_2 = Guest("Sarah", 26)
        guest_3 = Guest("Tom", 22)
        guest_4 = Guest("Lyla", 28)
        self.room_2.check_in(guest_1)
        self.room_2.check_in(guest_2)
        self.room_2.check_in(guest_3)
        self.room_2.check_in(guest_4)
        self.assertEqual("Sorry there is no more room!", self.room_2.capacity())

    def test_room_caps_at_3(self):
        self.assertEqual("full", self.room_1.capacity_cannot_go_over())

