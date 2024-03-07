from .CreditCard import CreditCard

class Bank:
    def __init__(self,name):
        self.__name = name
        self.__account_id_list = []
        self.__paypal_id_list = []
        self.__card_list = []

    def get_name(self):
        return self.__name

    def get_account_id_list(self):
        return self.__account_id_list

    def get_paypal_id_list(self):
        return self.__paypal_id_list

    def get_card_list(self):
        return self.__card_list

    def add_account_id(self,account_id):
        if isinstance(account_id,str):
            self.__account_id_list.append(account_id)
            return "Account id adding success in list"
        return "Account id adding error in list"

    def add_paypal_id(self,paypal_id):
        if isinstance(paypal_id,str):
            self.__paypal_id_list.append(paypal_id)
            return "Paypal id adding success in list"
        return "Paypal id adding error in list"

    def add_credit_card(self,card):
        if isinstance(card,CreditCard):
            self.__card_list.append(card)
            return "A Credit Card adding success in list"
        return "A Credit Card adding error in list"