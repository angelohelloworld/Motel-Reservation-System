import random, string
from prettytable import PrettyTable
from read_file import ReadFile
from write_file import WriteFile

class Manager:
    ROOM_FILE_NAME = "db-rooms.txt"
    RESERVATION_FILE_NAME = "db-reservations.txt"
    
    def __init__(self):
        self.readFile = ReadFile() 
        self.writeFile = WriteFile()
        
        self._rooms = []
        self._reservations = []
    
        self.read_rooms()
        self.read_reservations()
    
    def read_rooms(self):
        self.readFile.read_rooms(self.ROOM_FILE_NAME)
        self._rooms = self.readFile.get_rooms();
        
    def read_reservations(self):
        self.readFile.read_reservations(self.RESERVATION_FILE_NAME)
        self._reservations = self.readFile.get_reservations();
    
    def get_rooms(self):
        return self._rooms      
    
    def add_reservation(self, reservation):
        self._reservations.append(reservation)
        self.writeFile.write_reservation(self.RESERVATION_FILE_NAME, reservation);
    
    def update_num_of_guests(self, index, num_of_guests):
        self._reservations[index].set_num_of_guests(num_of_guests)
        self.writeFile.write_reservations(self.RESERVATION_FILE_NAME, self._reservations)
        
    def delete_reservation(self, index):
        del self._reservations[index]
        self.writeFile.write_reservations(self.RESERVATION_FILE_NAME, self._reservations)
	    
    def retrieve_booking(self, reservation_number):        
        for i, reservation in enumerate(self._reservations):
            if reservation.get_reservation_number() == reservation_number:
                return i, reservation
        
        return None, None
    
    def retrieve_room(self, name, check_in):
        for room in self._rooms:
            if (room.get_name() == name and
               room.get_check_in() == check_in):
               return room
               
        return None
        
    #Helpers
    def generate_reservation_number(self):
        reservation_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return reservation_number
    
    def is_reservation_exist(self, date, room_number, check_in):
        if len(self._reservations) != 0:
            for reservation in self._reservations:
                if (reservation.get_date() == date and 
                    reservation.get_room_number() == room_number and 
                    reservation.get_check_in() == check_in):
                    return True
        return False