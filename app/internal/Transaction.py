class Transaction:
    def __init__(self, amount, created_at, transaction_id, status):
        self.__amount = amount
        self.__created_at = created_at
        self.__transaction_id = transaction_id
        self.__status = status
        #Transaction Status: Unpaid,paid,cancelled

    def get_amount(self):
        return self.__amount
    
    def get_created_at(self):
        return self.__created_at

    def get_transaction_id(self):
        return self.__transaction_id

    def get_status(self):
        return self.__status

    def set_amount(self,amount):
        if isinstance(amount,int):
            self.__amount = amount
            return "Amount Setting success"
        return "Amount setting error"

    def set_created_at(self,date_input):
        if isinstance(date_input,str):
            self.__created_at = date_input
            return "Date Setting Success"
        return "Date setting error"

    def set_status(self,status):
        if isinstance(status,str): #and (status == "Unpaid" or status == "Paid" or status == "Canceled"):
            self.__status = status
            return "Status Setting success"
        return "Status Setting Error"