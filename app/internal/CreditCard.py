class CreditCard:
    def __init__(self, card_id, balance):
        self.__card_id = card_id
        self.__balance = balance
    
    def get_card_id(self):
        return self.__card_id
    
    def get_balance(self):
        return self.__balance
    
    def set_amount(self, balance):
        self.__balance = balance