class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.playlist = []
        self.number_guests = []




    def song_count(self):
        return len(self.playlist)

    def add_song(self, song):
        self.playlist.append(song)
        

    