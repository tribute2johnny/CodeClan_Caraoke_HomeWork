class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.playlist = []
        self.number_guests = []




    def song_count(self):
        return len(self.playlist)

    def add_song(self, song):
        self.playlist.append(song)

    def guest_count(self):
        return len(self.number_guests)
        
    def check_in(self, guest):
        self.number_guests.append(guest)

    def check_out(self, guest):
        self.number_guests.remove(guest)

