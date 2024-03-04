from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from .Person import Person

class Customer(Person):
    def __init__(self, firstname, lastname, country, province, zip_code, birthday, phone_number, account):
        super().__init__(firstname, lastname, country, province, zip_code, birthday, phone_number, account)
        self.__coupon_list = []
        self.__booking_list = []
        self.__my_favorite_hotel_list = []

    #Request จากคนทำ payment ขอเพิ่ม attribute account_id,bank,paypal_id เพื่อนำไปเช็คกับ argument ใน Method select_transaction()
    #ส่วนนี้ผู้ใช้จะกรอกมาตอนจะจ่ายตังเอง ไม่ต้องมีก็ได้นะ เว้นแต่จะทำ 'บันทึกเป็นบัตรที่ใช้ประจำ'  -fluk
    #Request จากคนทำ payment ขอ้เปลี่ยน attribute จาก Coupon เป็น Coupon list และมั Method add_coupon()
    #OKKKKK -fluk
    #Request จากคนทำ payment ขอ้เพิ่ม attribute balance เพื่อเก็บจำนวนเงินทั้งหมดของลูกค้า
    #ยังไม่มั่นใจ
        
    def get_coupon_list(self):
        return self.__coupon_list
        
    def get_booking_list(self):
        return self.__booking_list
    
    def get_my_favorite_hotel_list(self):
        return self.__my_favorite_hotel_list
    
    def add_coupon(self, coupon):
        # Validation
        self.__coupon_list.append(coupon)
    
    def add_booking(self, booking):
        # validation
        self.__booking_list.append(booking)
    
    def add_favorite_hotel(self, hotel):
        # Validation
        self.__my_favorite_hotel_list.append(hotel)    

        

    # def search_transaction(self,booking_no):
    #     for booking in self.__booking_list:
    #         if booking.get_booking_no() == booking_no:
    #             json = {}
    #             if isinstance(booking.get_transaction(),CreditCardTransaction):
    #                 json["Your Transaction"] = {'Transaction number' : booking.get_transaction().get_transaction_id(),
    #                                         'Transaction amount' : booking.get_transaction().get_amount(),
    #                                         'Transaction Status' : booking.get_transaction().get_status(),
    #                                         'Transaction Date' : booking.get_transaction().get_created_at(),
    #                                         'Credit Card Number' : booking.get_transaction().get_card_id(),
    #                                         'Credit Card CVV' : booking.get_transaction().get_cvv()}

    #             elif isinstance(booking.get_transaction(),MobileBankTransaction):
    #                 json["Your Transaction"] = {'Transaction number' : booking.get_transaction().get_transaction_id(),
    #                                         'Transaction amount' : booking.get_transaction().get_amount(),
    #                                         'Transaction Status' : booking.get_transaction().get_status(),
    #                                         'Transaction Date' : booking.get_transaction().get_created_at(),
    #                                         'Customer Bank Account ID' : booking.get_transaction().get_account_id(),
    #                                         'Customer Bank' : booking.get_transaction().get_bank()}

    #     elif isinstance(self.__current_booking.get_transaction(),PaypalTransaction):
    #         json["Your Transaction"] = {'Firstname' : self.__current_booking.get_firstname(),
    #                                 'Lastname' : self.__current_booking.get_lastname(),
    #                                 'Booking number' : self.__current_booking.get_booking_no(),
    #                                 'Hotel' : self.__current_booking.get_hotel().get_name(),
    #                                 'Room Type' : self.__current_booking.get_room_type(),
    #                                 'Room Amount' : self.__current_booking.get_room_quantity(),
    #                                 'Status' : self.__current_booking.get_status(),
    #                                 'Transaction number' : booking.get_transaction().get_transaction_id(),
    #                                 'Transaction amount' : booking.get_transaction().get_amount(),
    #                                 'Transaction Status' : booking.get_transaction().get_status(),
    #                                 'Transaction Date' : booking.get_transaction().get_created_at(),
    #                                 'Hotel Email Address' : booking.get_hotel().get_hotel_email(),
    #                                 'Customer Email Address' : booking.get_transaction().get_customer_email(),
    #                                 'Customer Paypal ID' : booking.get_transaction().get_paypal_id()}
    #     return json
        