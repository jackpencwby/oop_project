class Room:
    def __init__(self, room_no, type, price):
        self.__room_no = room_no
        self.__status = None
        self.__type = type      #small, medium, large
        self.__price = price
        self.__reserved_interval = []
        self.__pending_interval = []
    
    def get_room_no(self):
        return self.__room_no
    
    def get_status(self):
        return self.__status
    
    def get_type(self):
        return self.__type
    
    def get_price(self):
        return self.__price
    
    def change_status(self, status):
        # Validation
        self.__status = status

    def is_available_at(self, interval):
        return True

    