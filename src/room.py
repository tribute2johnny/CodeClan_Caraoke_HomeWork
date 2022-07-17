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

    # refactored this into the code below as it passes all 3 capacity tests 
    # def capacity_reached(self):
    #     if len(self.number_guests) == 3:
    #         return "room is full"
    #     else:
    #         return "room has space"

    def capacity(self):
        
        while len(self.number_guests) < 3:
            return "room has space"
        if len(self.number_guests) == 3:
            return "capacity reached"
        elif len(self.number_guests) > 3:
            return "Sorry there is no more room!"


    # attempt at trying to get the list to stop populating once it hit's a certain number
    def capacity_cannot_go_over(self):
        guests = ["dave", "sarah", "tim", "jane"]
        capacity = 0
        while capacity < 3:
            for guest in guests:
                capacity += 1
                if capacity > 3: 
                    return "full"
                self.number_guests.append(guest)

        
                
