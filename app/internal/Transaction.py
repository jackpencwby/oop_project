from fastapi import HTTPException, status
from datetime import date
from .Coupon import Coupon

class Transaction:
    def __init__(self, amount, created_at, transaction_id, status):
        self.__amount = amount
        self.__created_at = created_at
        self.__transaction_id = transaction_id
        self.__status = status
        self.__coupon_used = None
        #Transaction Status: unpaid, paid, cancelled
    
    def get_amount(self):
        return self.__amount
    
    def get_created_at(self):
        return self.__created_at

    def get_transaction_id(self):
        return self.__transaction_id

    def get_status(self):
        return self.__status
    
    def get_id(self):
        return self.__transaction_id
    
    def get_coupon_used(self):
        return self.__coupon_used

    def add_coupon(self, coupon):
        if isinstance(coupon, Coupon):
            self.__coupon_used = coupon
            return
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = {'message':'failed to set coupon to transac'})

    def set_amount(self, amount): 
        if isinstance(amount, int):
            self.__amount = amount
            return "Amount Setting success"
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = {'message':'failed to set transaction amount'})

    def set_created_at(self, date_input): 
        if isinstance(date_input, date):
            self.__created_at = date_input
            return "Date Setting Success"
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = {'message':'failed to set date'})

    def set_status(self, status): # 
        if isinstance(status, str) and (status == "unpaid" or status == "paid" or status == "cancelled"):
            self.__status = status
            return "Status Setting success"
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = {'message':'failed to set status'})