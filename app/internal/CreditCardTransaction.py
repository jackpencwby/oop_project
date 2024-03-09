from .Transaction import Transaction

class CreditCardTransaction(Transaction):
    def __init__(self, amount,created_at,transaction_id,status,card_id,cvv):
        Transaction.__init__(self,amount,created_at,transaction_id,status)
        self.__card_id = card_id
        self.__cvv = cvv


    def get_card_id(self):
        return self.__card_id

    def get_cvv(self):
        return self.__cvv
    
