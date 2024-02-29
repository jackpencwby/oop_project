from .Interval import Interval

class Room:
    def __init__(self, room_no, type, price):
        self.__room_no = room_no
        self.__type = type
        self.__price = price
        self.__status = None
        self.__reserved_interval = []
        self.__pending_interval = []
    
    def get_room_no(self):
        return self.__room_no
    
    def get_type(self):
        return self.__type
    
    def get_price(self):
        return self.__price
    
    def get_status(self):
        return self.__status
    
    def change_status(self, status):
        # Validation
        self.__status = status

    def is_available_at(self, interval):    #check both reserved, pending -- Fluk
        checkin = interval.get_begin_date()
        checkout = interval.get_end_date()
        for room_interval in self.__reserved_interval + self.__pending_interval:
            reserved_checkin = room_interval.get_begin_date()
            reserved_checkout = room_interval.get_end_date()
            if (checkin > reserved_checkin and checkin < reserved_checkout) or (checkout > reserved_checkin and checkout < reserved_checkout):
                return False
        return True

    # def add_pending_interval(self, interval):
    #     self.__pending_interval.append(interval)

    