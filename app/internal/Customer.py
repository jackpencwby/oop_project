from .Person import Person

class Customer(Person):
    def __init__(self, firstname, lastname, country, province, zip_code, birthday, phone_number, account):
        super().__init__(firstname, lastname, country, province, zip_code, birthday, phone_number, account)
        self.__credit_card = None
        self.__coupon = None
        self.__booking_list = []
        self.__my_favolite_hotel = []
    
    def get_credit_card(self):
        return self.__credit_card
    
    def get_coupon(self):
        return self.__coupon
    
    def get_booking_list(self):
        return self.__booking_list

    def add_credit_card(self, credit_card):
        # Validation
        self.__credit_card = credit_card
    
    def add_coupon(self, coupon):
        # Validation
        self.__coupon = coupon

    def add_booking(self, booking):
        # validation
        self.__booking_list.append(booking)

    def get_personal_information(self):
        return {"firstname": self.get_firstname(),
                "lastname": self.get_lastname(),
                "email": self.get_account().get_email(),
                "country": self.get_country(),
                "province": self.get_province(),
                "zip_code": self.get_zip_code(),
                "birthday": self.get_birthday(),
                "phone_number": self.get_phone_number()}
    
    def get_my_travelling(self):
        arriving = []
        cancelled = []
        for booking in self.__booking_list:
            if(booking.get_status() == "paid"):
                arriving.append({"firstname": booking.get_firstname(),
                                 "lastname": booking.get_lastname(),
                                 "booking_no": booking.get_booking_no(),
                                 "room_type": booking.get_room_type(),
                                 "room_quantity": booking.get_room_quantity(),
                                 "check_in_date": booking.get_interval().get_begin_date(),
                                 "check_out_date": booking.get_interval().get_end_date()})
            elif(booking.get_status() == "cancel"):
                cancelled.append({"firstname": booking.get_firstname(),
                                 "lastname": booking.get_lastname(),
                                 "booking_no": booking.get_booking_no(),
                                 "room_type": booking.get_room_type(),
                                 "room_quantity": booking.get_room_quantity(),
                                 "check_in_date": booking.get_interval().get_begin_date(),
                                 "check_out_date": booking.get_interval().get_end_date()})
        return {"arriving": arriving, "cancelled": cancelled}
    
    def add_my_favorite_hotel(self, hotel):
        self.__my_favolite_hotel.append(hotel)

    def get_my_favorite_hotel(self):
        my_favorite_hotel = []
        for hotel in self.__my_favolite_hotel:
            my_favorite_hotel.append(hotel.get_name())
        return my_favorite_hotel
            
    def booking(self):
        pass

    def cancle_booking(self):
        pass
    