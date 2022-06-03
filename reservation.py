class Reservation:
    def __init__(self, room_number, date, guest_name, num_of_guests, check_in, check_out, reservation_number):
        self._room_number = room_number
        self._date = date
        self._guest_name = guest_name
        self._num_of_guests = num_of_guests
        self._check_in = check_in
        self._check_out = check_out
        self._reservation_number = reservation_number
    
    def get_room_number(self):
        return self._room_number
    
    def get_date(self):
        return self._date
    
    def get_guest_name(self):
        return self._guest_name
        
    def get_num_of_guests(self):
        return self._num_of_guests
        
    def get_check_in(self):
        return self._check_in
        
    def get_check_out(self):
        return self._check_out
    
    def get_reservation_number(self):
        return self._reservation_number
        
    def set_num_of_guests(self, num_of_guests):
        self._num_of_guests = num_of_guests
        
    def to_string(self):
        return self._room_number + ',' + self._date + ',' + self._guest_name + ',' + str(self._num_of_guests) + ',' + self._check_in + ',' + self._check_out + ',' + self._reservation_number