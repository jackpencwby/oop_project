from .Payment import Transaction

class MobileBankTransaction(Transaction):
     def __init__(self,amount,created_date,transaction_id,status,account_id,bank):
        super().__init__(self,amount,created_date,transaction_id,status)
        self.__account_id = account_id
        self.__bank = bank
        self.__paytype = "Mobile Banking"

    def get_account_id(self):
        return self.__account_id
    def get_bank(self):
        return self.__bank