from fastapi import HTTPException, status
from .Transaction import Transaction

class MobileBankTransaction(Transaction):
    def __init__(self, amount, created_at, transaction_id, status, account_id, bank):
        Transaction.__init__(self, amount, created_at, transaction_id, status)
        self.__account_id = account_id
        self.__bank = bank

    def get_account_id(self):
        return self.__account_id

    def get_bank(self):
        return self.__bank
    
    def get_pay_type(self):
        return "Mobile Banking"