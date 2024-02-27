class Person:
    def __init__(self, fname, lname, citizen_id, phone_number):
        self.__fname = fname
        self.__lname = lname
        self.__citizen_id = citizen_id
        self.__phone_number = phone_number
        self.__account_list = []
        self.__credit_card_list = []
    
    def get_fname(self):
        return self.__fname
    
    def get_lname(self):
        return self.__lname
    
    def get_citizen_id(self):
        return self.__citizen_id
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_account_list(self):
        return self.__account_list
    
    def get_credit_card_list(self):
        return self.credit_card_list
    
    def add_account_list(self, account):
        # Validation
        self.__account_list.append(account)
    
    def add_credit_card(self, credit_card):
        # Validation
        self.__credit_card_list.append(credit_card)
        

    