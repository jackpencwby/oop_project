from .Interval import Interval

class Transaction:
    def __init__(self,transaction_id,booking_no,amount,created_date,status):
        self.__booking_no = booking_no
        self.__amount = amount
        self.__created_date = created_date
        self.__transaction_id = transaction_id
        self.__status = status
        self.__paytype = paytype
        # transaction status : "pending","paid","canceled"

        def get_booking_no(self):
            return self.__booking_no

        def set_amount(self,amount):
            if isinstance(amount,int):
                self.__amount = amount
                return "Amount Setting Success"
            return "Amount Setting Error"

        def set_created_date(self,date):
            if isinstance(date,Interval):
                self.__created_date = date
                return "Created Date Setting Success"
            return "Created Date Setting Error"

        def set_status(self,status):
            if isinstance(status,str):
                self.__status = status
                return "Status Setting Success"
            return "Status Setting Error"