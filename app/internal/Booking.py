class Booking:
    def __init__(self, firstname, lastname, booking_no, hotel, room_type, room_quantity, interval, status, payment=None):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__booking_no = booking_no
        self.__hotel = hotel
        self.__room_type = room_type
        self.__room_quantity = room_quantity
        self.__interval = interval   
        self.__status = status  # status: cancelled, pending, wait_for_checkin, wait_for_checkout
        self.__payment = payment

    def get_firstname(self):
        return self.__firstname
    
    def get_lastname(self):
        return self.__lastname
    
    def get_booking_no(self):
        return self.__booking_no
    
    def get_hotel(self):
        return self.__hotel
    
    def get_room_type(self):
        return self.__room_type

    def get_room_quantity(self):
        return self.__room_quantity

    def get_interval(self):
        return self.__interval
    
    def get_status(self):
        return self.__status
    
    def get_payment(self):
        return self.__payment
    
    def set_payment(self, payment):
        self.__payment = payment
    
    def set_status(self, status):
        # Validation
        self.__status = status
