from .Hotel import Hotel
from .Customer import Customer
from .Account import Account
from .Booking import Booking
from fastapi import HTTPException

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
    
    def add_person(self, person):
        # Validation
        self.__person_list.append(person)

    def add_hotel(self, hotel):
        # Validation
        self.__hotel_list.append(hotel)

    def login(self, email, password): #Bright
        for person in self.__person_list:
            if email == person.get_account().get_email():
                if password == person.get_account().get_password():
                    return {"Welcome"}
                return {"You enter wrong password"}
        return {"Not found"}
    
    def register(self, firstname, lastname, country, province, zip_code, birthday, phone_number, email, password, confirm_password): #Bright
        for person in self.__person_list:
            if email == person.get_account().get_email():
                return "Email is already exist"
        if password == confirm_password:
            account = Account(email, password, "customer")
            customer = Customer(firstname, lastname, country, province, zip_code, birthday, phone_number, account)
            self.__person_list.append(customer)
            return {"Register Successful"}
        return {"Not the same password"}

    def get_nearby_hotel(self, location): #Bright
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
        for person in self.__person_list:
            if(person.get_account().get_role() == "customer"):  
                if(firstname == person.get_firstname() and lastname == person.get_lastname()):
                    for booking in person.get_booking_list():
                        if(booking_no == booking.get_booking_no() and check_in_date == booking.get_interval().get_begin_datetime()):
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
    
    def view_rate_from_hotel(self, hotel, interval, amount):
        room_list = hotel.get_available_room(interval, amount)
        json = {}
        for room in room_list:
            json[f'{room.get_type()} room type'] = {'price per night': room.get_price(),
                                                    'image': 'jpeg'}
        if len(json) == 0:
            return {'error': 'no room available'}
        return json

    # def select_room_from_hotel(self, hotel, interval, room_type, amount):
    #     hotel.select_room(interval, amount, room_type)
    #     room = hotel.get_room_info_by_type(room_type)
        
    #     pass #return price detail and payment prompt
    #     return {'room type':room_type,
    #             'interval':interval,
    #             'amount':amount,
    #             'summary of charges':}

    # # def (self, firstname, lastname, booking_no, room_type, room_quantityhotel):
    # #     if nself.hoitetel is inot in hotel; in  in hotelself.hote;l_lkist:
    #         __
    #         if roomroomisinstance()room_ty
        
    # and payment(roo,ohotel,room_type    )yself           )len() and isinstance()room_quy,int == roo,m_qwuuanitiytynti
    #         for person in self.__person_list:
    #             if person.get_firstname() == firstname and person.gettlastname() == lastname:y:
                        
                        