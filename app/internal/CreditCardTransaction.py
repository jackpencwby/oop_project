from .Transaction import Transaction

class CreditCardTransaction(Transaction):
     def __init__(self,amount,created_date,transaction_id,status,card_id,key):
        super().__init__(self,amount,created_date,transaction_id,status)
        self.__card_id = card_id
        self.__key = key
        self.__paytype = "Credit Card"

        #Key means CVV (3 digits behind the credit card) not pin
        def get_card_id(self):
            return self.__card_id = card_id
        def get_key(self):
            return self.__key = key

