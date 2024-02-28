class Booking:
    def __init__(self, firstname, lastname, booking_no, room_type, room_quantity, interval, status):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__booking_no = booking_no
        self.__room_type = room_type
        self.__room_quantity = room_quantity
        self.__interval = interval   
        self.__status = status  #3 status: cancel, pending, paid

    def get_firstname(self):
        return self.__firstname
    
    def get_lastname(self):
        return self.__lastname
    
    def get_booking_no(self):
        return self.__booking_no
    
    def get_room_type(self):
        return self.__room_type

    def get_room_quantity(self):
        return self.__room_quantity

    def get_interval(self):
        return self.__interval
    
    def get_status(self):
        return self.__status
    
    def change_status(self, status):
        # Validation
        self.__status = status
