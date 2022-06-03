from prettytable import PrettyTable
from manager import Manager
from reservation import Reservation

class Menu:
    def __init__(self):
        self.manager = Manager()
        
    def view_rooms(self):
        rooms = self.manager.get_rooms()
        field_names = ["Room Number", "Description", "Check in", "Check out", "Capacity"]
        
        print("AVAILABLE ROOMS")
        self.displayRoomTable(rooms)
    
    def book_room(self):
        is_booking = True
        
        print("BOOK A ROOM")
            
        print("Name: ")
        guest_name = input()
        
        while is_booking == True:
            print("Check in Date(mm/dd/yyyy): ")
            date = input()
            print("Select Room Number: ")
            
            rooms = self.manager.get_rooms()
            for i, room in enumerate(rooms):
                print("[{0}]".format(str(i+1)), 
                        room.get_name(),
                        "(",
                        room.get_check_in(),
                        "-", 
                        room.get_check_out(),
                        ")")
            
            number = int(input())
            room_number = rooms[number-1].get_name()
            room_description = rooms[number-1].get_description()
            check_in = rooms[number-1].get_check_in()
            check_out = rooms[number-1].get_check_out()
            
            #if reservation exists
            if self.manager.is_reservation_exist(date, room_number, check_in):
                print("Sorry.", room_number, "is already booked on", date, check_in)
                continue
            
            print("Number of guests: ")
            num_of_guests = int(input())
            
            if rooms[number-1].get_capacity() < num_of_guests:
                print("Cannot add number of guests. It is beyond the capacity.")
                continue
            
            is_booking = False
        
        reservation_number = self.manager.generate_reservation_number()
        
        reservation = Reservation(room_number, date, guest_name, num_of_guests, check_in, check_out, reservation_number)
        self.manager.add_reservation(reservation);
        
        print(room_number,
            "successfully reserved for {0}.".format(str(date)),
            "Here's your reservation number:", 
            reservation_number)
    
    def manage_booking(self):
        print("MANAGE BOOKING")
        
        print("Enter reservation number(6 characters): ")
        reservation_number = input().upper()
        
        i, booking = self.manager.retrieve_booking(reservation_number)
        
        if booking == None :
            print("Booking not found.")
            return
        
        self.displayReservationTable(booking)
        
        print("[1] Update number of guests")
        print("[2] Cancel booking")
        
        action = int(input())
        
        if action == 1:
            self.edit_booking(i, booking)
        elif action == 2:
            self.cancel_booking(i, booking)
    
    def edit_booking(self, i, booking):
        is_edit = True
        
        while is_edit == True:
            print("Enter new number of guests:")
            num_of_guests = int(input())
            
            room = self.manager.retrieve_room(booking.get_room_number(), booking.get_check_in())
            
            if room.get_capacity() < num_of_guests:
                print("Cannot update number of guests. It is beyond the capacity.")
                continue
            
            is_edit = False
            
        self.manager.update_num_of_guests(i, num_of_guests)
        print("Booking", booking.get_reservation_number(),"successfully updated.")
        
        self.displayReservationTable(booking)
        
    def cancel_booking(self, i, booking):        
        print("Are you sure you want to cancel your booking?")
        
        print("[1] Yes")
        print("[2] No")
        
        action = int(input())
        
        if action == 1:
            self.manager.delete_reservation(i)
            print("Booking", booking.get_reservation_number(),"successfully cancelled.")
        elif action == 2:
            self.manage_booking()
            
    #Helpers
    def displayRoomTable(self, rooms):
        table = PrettyTable()
        table.field_names = ["Room Number", "Description", "Check in", "Check out", "Capacity"]
        table.align = "l"
        
        for room in rooms:
            table.add_row([
                room.get_name(), 
                room.get_description(), 
                room.get_check_in(), 
                room.get_check_out(), 
                room.get_capacity()
            ])
        print(table)
    
    def displayReservationTable(self, reservation):
        table = PrettyTable()
        table.field_names  = ["Room Number", "Date", "Guest Name", "No. of Guests", "Check in", "Check out", "Booking Number"]
        table.align = "l"
        
        table.add_row([
            reservation.get_room_number(), 
            reservation.get_date(), 
            reservation.get_guest_name(), 
            reservation.get_num_of_guests(), 
            reservation.get_check_in(), 
            reservation.get_check_out(), 
            reservation.get_reservation_number()
        ])
        
        print(table)