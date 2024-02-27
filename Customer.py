from Person import Person

class Customer(Person):
    def __init_(self):
        super().__init__()
        self.__account_list = []
        self.__credit_card_list = []
    
    def get_account_list(self):
        return self.__account_list
    
    def get_credit_card_list(self):
        return self.__credit_card_list
    
    def add_account(self, account):
        # Validation
        self.__account_list.append(account)

    def add_credit_card(self, credit_card):
        # Validation
        self.__credit_card_list.append(credit_card)

    def booking(self):
        pass

    def cancle_booking(self):
        pass