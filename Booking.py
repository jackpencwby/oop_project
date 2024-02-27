class Booking:
    def __init__(self, booking_no, check_in_date, check_out_date, status):
        self.__booking_no = booking_no
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__status = status
    
    def get_booking_no(self):
        return self.__booking_no
    
    def get_check_in_date(self):
        return self.__check_in_date
    
    def get_check_out_date(self):
        return self.__check_out_date
    
    def get_status(self):
        return self.__status
    
    def change_status(self, status):
        # Validation
        self.__status = status