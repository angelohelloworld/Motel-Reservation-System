class Room:
    def __init__(self, id, name, description, check_in, check_out, capacity):
        self._id = id
        self._name = name
        self._description = description
        self._check_in = check_in
        self._check_out = check_out
        self._capacity = capacity

    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name
    
    def get_description(self):
        return self._description
        
    def get_check_in(self):
        return self._check_in
    
    def get_check_out(self):
        return self._check_out
    
    def get_capacity(self):
        return int(self._capacity)