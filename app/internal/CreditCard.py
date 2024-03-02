class CreditCard:
    def __init__(self,card_id,key,customer):
        self.__card_id = card_id
        self.__key = key
        self.__customer = customer
    
    def get_card_id(self):
        return self.__card_id
    
    def get_key(self):
        return self.__key