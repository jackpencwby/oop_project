from Customer import Customer

class Company:
    def __init__(self, name):
        self.__name = name
        self.__person_list = []
        self.__hotel_list = []

    def get_name(self):
        return self.__name
    
    def get_person_list(self):
        return self.__person_list
    
    def get_hotel_list(self):
        return self.__hotel_list
    
    def add_person(self, account):
        # Validation
        self.__account_list.append(account)

    def add_hotel(self, hotel):
        # Validation
        self.__hotel_list.append(hotel)

    def login(self, email, password):
        for person in self.__person_list:
            account = person.get_account()
            if email == account.get_email():
                if password == account.get_password():
                    return {"Welcome"}
                else: return {"You enter wrong password"}
        return {"Not found"}
    
    def register(self, firstname, lastname, country, province, zip_code, birthday, phone_number, email, password, confirmpassword):
        if password.len() < 6:
            if password == confirmpassword:
                person = Customer(firstname, lastname, country, province, zip_code, birthday, phone_number, None)
                self.__person_list.append(person)
                person.create_account(email, password)
                return {"Register Successful"}
            else: return {"Not the same password"}
        else: return {"Invalid password"}

    def get_nearby_hotel(self, location):
        nearby_hotel_list = []
        for hotel in self.__hotel_list:
            if hotel.get_location().get_province() == location or hotel.get_location().get_district() == location:
                nearby_hotel_list.append(hotel)
        return nearby_hotel_list
    
    def add_opinion(self, hotel_name, comment, rating):
        if 0 > rating > 5:
            return "Invalid rating"
        for hotel in self.__hotel_list:
            if hotel.get_hotel_name() == hotel_name:
                hotel.append_opinion(comment, rating)
                return "Success", hotel.get_opinion()
        return "not found Hotel"

    def search_booking(self, firstname, lastname, booking_no, check_in_date): 
        for person in self.__person_list():
            if(firstname == person.get_firstname() and lastname == person.get_lastname()):
                for booking in person.get_booking_list():
                    if(booking_no == booking.booking_no and check_in_date == booking.get_interval().get_begin_datetime()):
                        return {"firstname": booking.get_firstname(), 
                                "lastname": booking.get_lastname(),
                                "booking_no": booking.get_booking_no(),
                                "room_type": booking.get_room_type(),
                                "room_quantity": booking.get_room_quantity(),
                                "check_in_date": booking.get_interval().get_begin_datetime(),
                                "check_out_date": booking.get_interval().get_end_datetime(),
                                "status": booking.get_status()}
                return None
        return None
    
    # def view_rate(self, hotel, interval, amount):
    #     example = hotel.get_available_room(interval, amount)
    #     json = {}
    #     for room in example:
    #         json[f'{room.get_type()} room type'] = {'room no.': room.get_room_no(),
    #                                                 'type': room.get_type(),
    #                                                 'price per night': room.get_price()}
    #     return json

    # def select(self, room_type):
    #     pass

    # # def (self, firstname, lastname, booking_no, room_type, room_quantityhotel):
    # #     if nself.hoitetel is inot in hotel; in  in hotelself.hote;l_lkist:
    #         __
    #         if roomroomisinstance()roo,m_ty
        
    # and payment(roo,ohotel,room_type    )yself           )len() and isinstance()room_quy,int == roo,m_qwuuanitiytynti
    #         for person in self.__person_list:
    #             if person.get_firstname() == firstname and person.gettlastname() == lastname:y:
                        
                        