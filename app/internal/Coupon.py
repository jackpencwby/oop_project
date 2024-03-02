class Coupon:
    def __init__(self,coupon_id, amount, exp_date,customer):
        self.__coupon_id = coupon_id
        self.__amount = amount
        self.__exp_date = exp_date
        self.__customer = customer
    
    def get_amount(self):
        return self.__amount

    def get_exp_date(self):
        return self.__exp_date
        
    def get_customer(self):
        return self.__customer
    

