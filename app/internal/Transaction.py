from datetime import date 

class Transaction:
    def __init__(self,amount,transaction_id,status):
        self.__amount = amount
        self.__created_at = date.today()#Take no parameter and set to today
        self.__transaction_id = transaction_id
        self.__status = status
        self.__paytype = None
        #Transaction Status: Unpaid,paid,canceled

    def get_amount(self):
        return self.__amount
    
    def get_created_at(self):
        return self.__created_at

    def get_transaction_id(self):
        return self.__transaction_id

    def get_status(self):
        return self.__status

    def get_paytype(self):
        return self.__paytype

    def set_amount(self,amount):
        if isinstance(amount,int):
            self.__amount = amount
            return "Amount Setting success"
        return "Amount setting error"

    def set_booking_no(self,booking_id):
        if isinstance(booking_id,str):
            self.__booking_no = booking_id
            return "Booking id Setting success"
        return "Booking id setting error"

    def set_status(self,status):
        if isinstance(status,str):
            self.__status = status
            return "Status Setting success"
        return "Status Setting Error"