from fastapi import HTTPException, status
from .Transaction import Transaction

class Booking:
    def __init__(self, firstname, lastname, booking_no, hotel, room_type, room_quantity, interval, status, transaction=None):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__booking_no = booking_no
        self.__hotel = hotel
        self.__room_type = room_type
        self.__room_quantity = room_quantity
        self.__interval = interval   
        self.__status = status  #arriving, cancelled, passed, staying
        self.__transaction = transaction

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
    
    def get_transaction(self):
        return self.__transaction
    
    def set_transaction(self, transaction):
        if isinstance(transaction, Transaction):
            self.__transaction = transaction
            return "Transaction Setting Successed in Booking"
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = {'message':'Invalid transaction'})

    def set_status(self, status):
        if status == "cancelled" or status == "pending" or status == "wait_for_checkin" or status == "wait_for_checkout":
            self.__status = status
            return "Booking Status Setting Success"


