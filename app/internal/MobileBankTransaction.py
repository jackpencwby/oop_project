from .Transaction import Transaction

class MobileBankTransaction(Transaction):
    def __init__(self, amount, created_at, transaction_id,status,account_id,bank):
        Transaction.__init__(self, amount, created_at, transaction_id, status)
        self.__account_id = account_id
        self.__bank = bank

    def get_account_id(self):
        return self.__account_id

    def get_bank(self):
        return self.__bank
    
    def get_paytype(self):
        return "Mobile Banking"

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