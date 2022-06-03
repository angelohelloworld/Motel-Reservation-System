from room import Room
from reservation import Reservation

class ReadFile:
    def __init__(self):
        self._rooms = []
        self._reservations = []
        
    def get_rooms(self):
        return self._rooms
        
    def get_reservations(self):
        return self._reservations    
        
    def read_rooms(self, file_name):
        try:
            with open(file_name, "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    id = currentline[0]
                    name = currentline[1]
                    description = currentline[2]
                    check_in = currentline[3]
                    check_out = currentline[4]
                    capacity = currentline[5].strip()
                    
                    room = Room(id, name, description, check_in, check_out, capacity)
                    self._rooms.append(room)
                    
        except FileNotFoundError:
            print("No file exist")
    
    def read_reservations(self, file_name):
        try:
            with open(file_name, "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    room_number = currentline[0]
                    date = currentline[1]
                    guest_name = currentline[2]
                    num_of_guests = currentline[3]
                    check_in = currentline[4]
                    check_out = currentline[5]
                    reservation_number = currentline[6].strip()
                    
                    reservation = Reservation(room_number, date, guest_name, num_of_guests, check_in, check_out, reservation_number)
                    self._reservations.append(reservation)
                    
        except FileNotFoundError:
            print("No file exist") 