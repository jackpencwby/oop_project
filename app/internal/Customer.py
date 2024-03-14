from fastapi import HTTPException, status
from .Person import Person
from .Booking import Booking
from .Hotel import Hotel
from .Coupon import Coupon

class Customer(Person):
    def __init__(self, firstname, lastname, country, province, zip_code, birthday, phone_number, account):
        super().__init__(firstname, lastname, country, province, zip_code, birthday, phone_number, account)
        self.__coupon_list = []
        self.__booking_list = []
        self.__my_favorite_hotel_list = []
        
    def get_coupon_list(self):
        return self.__coupon_list
        
    def get_booking_list(self):
        return self.__booking_list
    
    def get_my_favorite_hotel_list(self):
        return self.__my_favorite_hotel_list
    
    def add_coupon(self, coupon):
        if isinstance(coupon, Coupon):
            self.__coupon_list.append(coupon)
            return
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = {'messsage': 'Invalid coupon'})
    
    def add_booking(self, booking):
        if isinstance(booking, Booking):
            self.__booking_list.append(booking)
            return
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = {'messsage': 'Invalid booking'})
            
    def remove_coupon(self, coupon): 
        if coupon in self.__coupon_list:
            self.__coupon_list.remove(coupon)
            return 
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = {'messsage': 'Coupon doesn\'t in account'})
    
    def add_favorite_hotel(self, hotel): 
        if isinstance(hotel ,Hotel):
            for hotel_index in self.__my_favorite_hotel_list:
                if hotel_index.get_name() == hotel.get_name():
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                        detail = {'messsage': 'Hotel already added'})
            self.__my_favorite_hotel_list.append(hotel)
            return
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail = {'messsage': 'Invalid Hotel'})

    def remove_favorite_hotel(self, hotel): 
        if isinstance(hotel ,Hotel) and hotel in self.__my_favorite_hotel_list:
            self.__my_favorite_hotel_list.remove(hotel)   
            return
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail = {'message': 'This hotel isn\'t in favorite list'})

    def search_booking_by_id(self, booking_no): #เป็นการ return ออกไปที่ api ???
        for booking in self.__booking_list:
            if booking_no == booking.get_booking_no():
                return booking
        return None
    