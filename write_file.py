class WriteFile:
    def write_reservation(self, file_name, reservation):
        with open(file_name, "a") as filestream:
            filestream.write(reservation.to_string() + '\n')
    
    def write_reservations(self, file_name, reservations):
        with open(file_name, "w") as filestream:
            for reservation in reservations:
                    filestream.write(reservation.to_string() + '\n')