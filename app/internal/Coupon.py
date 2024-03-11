class Coupon:
    def __init__(self, coupon_id, amount, exp_date):
        self.__coupon_id = coupon_id
        self.__amount = amount
        self.__exp_date = exp_date
    
    def get_coupon_id(self):
        return self.__coupon_id

    def get_amount(self):
        return self.__amount

    def get_exp_date(self):
        return self.__exp_date

