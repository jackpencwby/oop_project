from datetime import date 

class Payment:
    def __init__(self, amount, created_at):
        self.__amount = amount
        self.__created_at = created_at

    def get_amount(self):
        return self.__amount
    
    def get_created_at(self):
        return self.__created_at
    