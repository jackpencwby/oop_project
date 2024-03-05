from .Transaction import Transaction

class PaypalTransaction(Transaction):
    def __init__(self, amount, created_at,transaction_id,status,customer_email,paypal_id):
        super().__init__(self, amount, created_at,transaction_id,status)
        self.__customer_email = customer_email
        self.__paypal_id = paypal_id
        self.__paytype = "Paypal"

    def get_customer_email(self):
        return self.__customer_mail

    def get_paypal_id(self):
        return self.__paypal_id

    def set_customer_email(self,email):
        if isinstance(email,str) and "@" in email:
            self.__customer_email = email
            return "Email Setting Success"
        return "Email Setting Error"
    
    def set_paypal_id(self,paypal_id):
        if isinstance(paypal_id,str):
            self.__paypal_id = paypal_id
            return "Paypal id Setting Success"
        return "Paypal_id Setting Error"
    