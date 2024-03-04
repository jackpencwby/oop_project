# from .Customer import Customer
# from .Transaction import Transaction

# class CreditCardTransaction(Transaction):
#     def __init__(self, amount,transaction_id,status,card_id,cvv):
#         super().__init__(self, amount,transaction_id,status)
#         self.__card_id = card_id
#         self.__cvv = ccv
#         self.__paytype = "Credit Card"

#     def get_card_id(self):
#         return self.__card_id

#     def get_cvv(self):
#         return self.__cvv

#     def set_card_id(self,card_id):
#         if isinstance(card_id,str):
#             self.__card_id = card_id
#             return "Card id Setting Success"
#         return "Card id Setting Error"
    
#     def set_ccv(self,cvv):
#         if isinstance(cvv,str) and len(cvv) == 3:
#             self.__cvv = cvv
#             return "CVV Setting Success"
#         return "CVV Setting Error"