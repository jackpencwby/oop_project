from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from datetime import date as Date
from .Customer import Customer
from .Account import Account
from .Interval import Interval
from ..utils.dependency import set_current_user

class Company:
    def __init__(self, name):
        self.__name = name
        self.__person_list = []
        self.__hotel_list = []
        
    #Request จากคนทำ Payment ขอเพิ่ม attribute temp_booking_list และ temp_transaction_list สำหรับเก็บไว้ชั่วคราว

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

    def login(self, email, password):
        for person in self.__person_list:
            if email == person.get_account().get_email():
                if password == person.get_account().get_password():
                    set_current_user(person)
                    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Login Successfully"})
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"message": "Wrong Password"})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"message": "Email doesn't exist"})
    
    def register(self, firstname, lastname, country, province, zip_code, birthday, phone_number, email, password, confirm_password): 
        for person in self.__person_list:
            if email == person.get_account().get_email():
                return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "Email already exist"})
        if password == confirm_password:
            account = Account(email, password, role="customer")
            customer = Customer(firstname, lastname, country, province, zip_code, birthday, phone_number, account)
            self.__person_list.append(customer)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Register Successfully"})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "Password doesn't match"})

    def search_nearby_hotel(self, country, province):
        nearby_hotel_list = []
        for hotel in self.__hotel_list:
            if hotel.get_location().get_country() == country and hotel.get_location().get_province() == province:
                nearby_hotel_list.append(hotel.get_name())
        return JSONResponse(status_code=status.HTTP_200_OK, content=nearby_hotel_list)

    def search_booking(self, firstname, lastname, booking_no, check_in_date):
        for person in self.__person_list:
            if(person.get_account().get_role() == "customer"):  
                if(firstname == person.get_firstname() and lastname == person.get_lastname()):
                    for booking in person.get_booking_list():
                        if(booking_no == booking.get_booking_no() and check_in_date == booking.get_interval().get_begin_date()):
                            return JSONResponse(status_code=status.HTTP_200_OK, content={"firstname": booking.get_firstname(), 
                                                                                                    "lastname": booking.get_lastname(),
                                                                                                    "booking_no": booking.get_booking_no(),
                                                                                                    "hotel_name": booking.get_hotel_name(),
                                                                                                    "room_type": booking.get_room_type(),
                                                                                                    "room_quantity": booking.get_room_quantity(),
                                                                                                    "check_in_date": booking.get_interval().get_begin_date(),
                                                                                                    "check_out_date": booking.get_interval().get_end_date(),
                                                                                                    "status": booking.get_status()})
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "No booking Information"})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "Firstname and Surname doesn't exist"})
    
    def add_opinion(self, hotel_name, comment, rating):
        if 0 > rating > 5:
            return "Invalid rating"
        for hotel in self.__hotel_list:
            if hotel.get_hotel_name() == hotel_name:
                hotel.append_opinion(comment, rating)
                return "Success", hotel.get_opinion()
        return "not found Hotel"
    
    def view_rate_from_hotel(self, hotel_name, date_list, amount):
        needed_hotel, interval = self.convert_hotel_and_interval(hotel_name, date_list)
        room_list = needed_hotel.get_available_room(interval, amount)
        json = {}
        for room in room_list:
            json[f'{room.get_type()} room type'] = {'price per night': room.get_price(),
                                                    'image': 'jpeg'}
        if len(json) == 0:
            return {'error': 'no room available'}
        return json

    def convert_hotel_and_interval(self, hotel_name, date_list):
        needed_hotel = None
        for hotel in self.__hotel_list:
            if hotel.get_name() == hotel_name:
               needed_hotel = hotel
               break
        by, bm, bd = [int(x) for x in date_list[0].split('-')]
        ey, em, ed = [int(x) for x in  date_list[1].split('-')]  
        interval = Interval(begin = Date(by, bm, bd), end = Date(ey, em, ed))
        return [needed_hotel, interval]
    
    def select_room(self, hotel_name, date_list, amount, room_type):
        needed_hotel, interval = self.convert_hotel_and_interval(hotel_name, date_list)
        needed_hotel.select_room(interval, amount, room_type)
        room = needed_hotel.get_room_by_type(room_type)
        return {'room type': room_type,
                'interval': interval,
                'amount': amount,
                'summary of charges': room.get_price()*amount*interval.get_night(),
                'night': interval.get_night()}
