import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("Cher", "Believe")
        self.song_2 = Song("The Cure", "Boys don't cry")
        self.song_3 = Song("Rick Astley", "Never gonna give you up")
        self.song_4 = Song("Blur", "Song 2")
        self.song_5 = Song("Bee Gees", "Staying alive")

    def test_song_has_artist(self):
        self.assertEqual("Cher", self.song_1.artist)

    def test_song_has_song_name(self):
        self.assertEqual("Song 2", self.song_4.song_name)