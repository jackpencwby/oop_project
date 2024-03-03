from .Transaction import Transaction

class MobileBankTransaction(Transaction):
    def __init__(self, amount,transaction_id,status,account_id,bank):
        super().__init__(self, amount,transaction_id,status)
        self.__account_id = account_id
        self.__bank = bank
        self.__paytype = "Mobile Banking"

    def get_account_id(self):
        return self.__account_id

    def get_bank(self):
        return self.__bank

    def set_account_id(self,account_id):
        if isinstance(account_id,str):
            self.__account_id = account_id
            return "Account id Setting Success"
        return "Account id Setting Error"
    
    def set_bank(self,bank):
        if isinstance(bank,str):
            self.__bank = bank
            return "Bank Setting Success"
        return "Bank Setting Error"