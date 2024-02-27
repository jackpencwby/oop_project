class Hotel:
    def __init__(self, name, location, room_list):
        self.__name = name
        self.__location = location
        self.__status = None
        self.__room_list = room_list

    def get_name(self):
        return self.__name
    
    def get_location(self):
        return self.__location
    
    def get_status(self):
        return self.__status
    
    def change_status(self, status):
        # Validation
        self.__status = status

    def get_room_list(self):
        return self.__room_list
    