class CreditCard:
    def __init__(self, card_id, cvv, balance):
        self.__card_id = card_id
        self.__cvv = cvv
        self.__balance = balance
    
    def get_card_id(self):
        return self.__card_id

    def get_cvv(self):
        return self.__cvv
    
    def get_balance(self):
        return self.__balance
    
    def set_amount(self, balance):
        self.__balance = balance