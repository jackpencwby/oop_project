class Room:
    def __init__(self, room_no):
        self.__room_no = room_no
        self.__status = None
    
    def get_room_no(self):
        return self.__room_no
    
    def get_status(self):
        return self.__status
    
    def change_status(self, status):
        # Validation
        self.__status = status