class CreditCard:
    credit_limit = 50000

    def __init__(self,card_id,key):
        self.__card_id = card_id
        self.__key = key
    
    def get_card_id(self):
        return self.__card_id
    def get_key(self):
        return self.__key