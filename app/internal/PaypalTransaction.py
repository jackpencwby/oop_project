from .Transaction import Transaction

class PaypalTransaction(Transaction):
     def __init__(self,amount,created_date,transaction_id,status,customer_email,paypal_id):
        super().__init__(self,amount,created_date,transaction_id,status)
        self.__customer_email = customer_email
        self.__hotel_email = hotel_email 
        self.__paypal_id = paypal_id
        self.__paytype = "Paypal"


    def get_customer_email(self):
        return self.__customer_email
    def get_paypal_id(self):
        return self.__paypal_id
    #def set_hotel_email(self,email)