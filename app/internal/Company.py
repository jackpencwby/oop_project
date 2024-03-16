from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from datetime import date
from .Person import Person
from .Customer import Customer
from .Admin import Admin
from .Account import Account
from .Interval import Interval 
from .Booking import Booking
from .Opinion import Opinion
from .Bank import Bank
from .Hotel import Hotel
from .CreditCardTransaction import CreditCardTransaction
from .MobileBankTransaction import MobileBankTransaction
from .PaypalTransaction import PaypalTransaction
from ..utils.dependency import set_current_user
from ..utils.dependency import get_current_user

class Company:
    def __init__(self, name, hotel_list):
        self.__name = name
        self.__person_list = []
        self.__hotel_list = hotel_list
        self.__bank_list = []
        self.__total = 0
        self.__current_hotel = None
        self.__current_booking = None
        self.__current_booking_id = "007"
        self.__current_transaction = None
        self.__current_transaction_id = "007"

    def add_person(self, person):
        if isinstance(person, Person):
            self.__person_list.append(person)
            return 'done'
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={'message':'Invalid person added'})

    def add_bank(self, bank):
        if isinstance(bank, Bank):
            self.__bank_list.append(bank)
            return "Bank Adding success in list"
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={'message':'Invalid bank added'})

    def reset_current_cache(self):
        if self.__current_booking: 
            self.__current_booking.get_hotel().cancel_pending_room(self.__current_booking)
        self.__current_hotel = None
        self.__total = 0
        self.__current_booking = None
        self.__current_transaction = None

    def login(self, email, password):
        for person in self.__person_list:
            if email == person.get_account().get_email():
                if password == person.get_account().get_password():
                    set_current_user(person)
                    if isinstance(person, Customer):
                        return JSONResponse(status_code=status.HTTP_200_OK, 
                                        content={"message": "Customer login Successfully",
                                                 'first_name':person.get_firstname(),
                                                 'last_name':person.get_lastname()})
                    else:
                        return JSONResponse(status_code=status.HTTP_200_OK, 
                                        content={"message": "Admin login Successfully",
                                                 'first_name':person.get_firstname(),
                                                 'last_name':person.get_lastname()})
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                    detail={"message": "Wrong Password"})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail={"message": "Email doesn't exist"})
    
    def logout(self, current_user):
        if(current_user == None):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail={"message": "Please login first"})
        self.reset_current_cache()
        set_current_user(None)
        return JSONResponse(status_code=status.HTTP_200_OK, 
                            content={"message": "Logout Successfully"}) 
    
    def register(self, firstname, lastname, country, province, zip_code, birthday, phone_number, email, password, confirm_password): 
        for person in self.__person_list:
            if email == person.get_account().get_email():
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                     detail={"message": "Email already exist"})
        if password == confirm_password:
            day, month, year = birthday.split("-")
            birthday_date = date(int(year), int(month), int(day))
            account = Account(email, password, role="customer")
            customer = Customer(firstname, lastname, country, province, zip_code, birthday_date, phone_number, account)
            self.__person_list.append(customer)
            return JSONResponse(status_code=status.HTTP_200_OK, 
                                content={"message": "Register Successfully"})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail={"message": "Password doesn't match"})
    
    def search_nearby_hotel(self, country, province):
        nearby_hotel_list = []
        for hotel in self.__hotel_list:
            if hotel.get_location().get_country() == country and hotel.get_location().get_province() == province:
                nearby_hotel_list.append({"hotel_name": hotel.get_name(),
                                          "location": {"country": hotel.get_location().get_country(), 
                                                       "province": hotel.get_location().get_province()}})
        if len(nearby_hotel_list) != 0:
            return JSONResponse(status_code=status.HTTP_200_OK, content={'hotel_list':nearby_hotel_list})
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message":'No hotel nearby'})

    def search_booking(self, firstname, lastname, booking_no, check_in_date):
        for person in self.__person_list:
            if(person.get_account().get_role() == "customer" and firstname == person.get_firstname() and lastname == person.get_lastname()):  
                for booking in person.get_booking_list():
                    if(booking_no == booking.get_booking_no() and check_in_date == booking.get_interval().get_begin_date().strftime("%d-%m-%Y")):
                        return JSONResponse(status_code=status.HTTP_200_OK, 
                                            content={"firstname": booking.get_firstname(),
                                                     "lastname": booking.get_lastname(),
                                                     "booking_no": booking.get_booking_no(),
                                                     "hotel":  {"hotel_name": booking.get_hotel(). get_name(),
                                                                 "location":{"country": booking.get_hotel().get_location().get_country(), 
                                                                            "province": booking.get_hotel().get_location().get_province()}},
                                                     "room_type": booking.get_room_type(),
                                                      "room_quantity": booking.get_room_quantity(),
                                                     "check_in_date": booking.get_interval().get_begin_date().strftime("%A %d %B %Y"),
                                                     "check_out_date": booking.get_interval().get_end_date().strftime("%A %d %B %Y"),
                                                     "status": booking.get_status()}) 
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,  
                                    detail={"message": "No booking Information"})  
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={"message": "Firstname and Surname doesn't exist"})  
     
    def get_personal_information(self, current_user):
        if(current_user == None): 
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail={"message": "Please login first"})
        return JSONResponse(status_code=status.HTTP_200_OK, 
                            content={"firstname": current_user.get_firstname(),
                                     "lastname": current_user.get_lastname(),
                                     "email": current_user.get_account().get_email(),
                                     "country": current_user.get_country(),
                                     "province": current_user.get_province(),
                                     "zip_code": current_user.get_zip_code(),
                                     "birthday": current_user.get_birthday().strftime("%A %d %B %Y"),
                                     "phone_number": current_user.get_phone_number()})
    
    def get_my_travelling(self, current_user):
        if(current_user == None):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail={"message": "Please login first"})
        if(isinstance(current_user, Admin)):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail={"message": "Admin doesn\'t have booking"})
        arriving = [] 
        cancelled = [] 
        for booking in current_user.get_booking_list():
            if(booking.get_status() == "arriving"):
                arriving.append({"firstname": booking.get_firstname(),
                                 "lastname": booking.get_lastname(),
                                 "booking_no": booking.get_booking_no(),
                                 "hotel": {"hotel_name": booking.get_hotel().get_name(),
                                            "location": {"country": booking.get_hotel().get_location().get_country(), 
                                                        "province": booking.get_hotel().get_location().get_province()}},
                                 "room_type": booking.get_room_type(), 
                                 "room_quantity": booking.get_room_quantity(),
                                 "check_in_date": booking.get_interval().get_begin_date().strftime("%A %d %B %Y"),
                                 "check_out_date": booking.get_interval().get_end_date().strftime("%A %d %B %Y")})
            elif(booking.get_status() == "cancelled"):
                cancelled.append({"firstname": booking.get_firstname(),
                                 "lastname": booking.get_lastname(),
                                 "booking_no": booking.get_booking_no(),
                                 "hotel": {"hotel_name": booking.get_hotel().get_name(),
                                           "location": {"country": booking.get_hotel().get_location().get_country(), 
                                                        "province": booking.get_hotel().get_location().get_province()}},
                                 "room_type": booking.get_room_type(),
                                 "room_quantity": booking.get_room_quantity(),
                                 "check_in_date": booking.get_interval().get_begin_date().strftime("%A %d %B %Y"),
                                 "check_out_date": booking.get_interval().get_end_date().strftime("%A %d %B %Y")})
        return JSONResponse(status_code=status.HTTP_200_OK, 
                            content={"arriving": arriving, 
                                     "cancelled": cancelled})  
 
    def get_my_favorite_hotel(self, current_user):
        if(current_user == None or not isinstance(current_user, Customer)):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail={"message": "Please login first"})
        my_favorite_hotel = []
        for hotel in current_user.get_my_favorite_hotel_list():
            my_favorite_hotel.append({"hotel_name": hotel.get_name(),
                                      "location": {"country": hotel.get_location().get_country(), 
                                                   "province": hotel.get_location().get_province()}})
        if len(my_favorite_hotel) != 0:
            return JSONResponse(status_code=status.HTTP_200_OK, 
                                content={'my_fav_hotel':my_favorite_hotel})
        return JSONResponse(status_code=status.HTTP_200_OK, 
                            content={"message": "There is no hotel you like"})
    
    def add_favorite_hotel(self, hotel_name, current_user):
        if(current_user == None):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail={"message": "Please login first"})
        for hotel in self.__hotel_list: 
            if hotel_name == hotel.get_name():
                current_user.add_favorite_hotel(hotel)
                return JSONResponse(status_code=status.HTTP_200_OK, 
                                    content={"message":"Add Successfully"})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail={"message": "Invalid hotel name"})
    
    def remove_favorite_hotel(self, hotel_name, current_user):
        if(current_user == None):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail={"message": "Please login first"})
        for hotel in self.__hotel_list: 
            if hotel_name == hotel.get_name():
                current_user.remove_favorite_hotel(hotel)
                return JSONResponse(status_code=status.HTTP_200_OK,
                                    content={"message":"Removed Successfully"})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail={"message": "Invalid hotel name"})
    
    def add_opinion(self, hotel_name, rating, comment, current_user):
        if(current_user == None):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail={"message": "Please login first"})
        
        if not isinstance(rating, int) or 0 > rating > 5 or not isinstance(comment, str):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                detail={"message": "Invalid rating or comment"})
        
        for hotel in self.__hotel_list:
            if hotel.get_name() == hotel_name:
                hotel.add_opinion(Opinion(rating, comment))
                return JSONResponse(status_code=status.HTTP_200_OK, 
                                    content={"message": "Add opinion successfully"})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail={"message": "Hotel not found"})
    
    def get_opinion(self, hotel_name):
        for hotel in self.__hotel_list:
            if hotel_name == hotel.get_name():
                if len(hotel.get_opinion()) == 0:
                    return JSONResponse(status_code=status.HTTP_200_OK, 
                                        content={"rating": "No rating",
                                                 "comment": "No comment"})
                else: 
                    return JSONResponse(status_code=status.HTTP_200_OK, 
                                        content={"rating": sum([int(opinion.get_rating()) for opinion in hotel.get_opinion()]) / len(hotel.get_opinion()),
                                                 "comment": [opinion.get_comment() for opinion in hotel.get_opinion()]})
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail={"message": "Invalid hotel name"})     

    def view_rate_from_hotel(self, hotel_name, date_list, amount):
        self.reset_current_cache()
        needed_hotel, interval = self.convert_hotel_and_interval(hotel_name, date_list)
        if amount > 3 or amount < 1 or not isinstance(amount, int):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail={"message": "amount error"})
        room_list = needed_hotel.get_available_room(interval, amount)
        json = {}

        for room in room_list:
            json[f'{room.get_type()} room type'] = {'price per night': room.get_price()}
        if len(json) == 0:
            return JSONResponse(status_code=status.HTTP_200_OK, 
                                content={'message': 'no room available'})
        return JSONResponse(status_code=status.HTTP_200_OK, 
                            content=json)

    def convert_hotel_and_interval(self, hotel_name, date_list):
        needed_hotel = None
        for hotel in self.__hotel_list:
            if hotel.get_name() == hotel_name:
                needed_hotel = hotel
                break
        if needed_hotel == None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                detail={"message": "Can't found hotel"})
        by, bm, bd = [int(x) for x in date_list[0].split('-')]
        ey, em, ed = [int(x) for x in date_list[1].split('-')]
        begin = date(by, bm, bd)
        end = date(ey, em, ed)
        if begin > date.today() and end > date.today() and end > begin:
            interval = Interval(begin = begin, end = end)
            return [needed_hotel, interval]
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail={"message": "Invalid date"})
    
    def select_room(self, hotel_name, date_list, amount, room_type):
        if get_current_user() == None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail={"message": "Please login first"})
        self.reset_current_cache()
        self.__current_hotel, interval = self.convert_hotel_and_interval(hotel_name, date_list)
        self.__current_hotel.select_room(interval, amount, room_type)
        room = self.__current_hotel.get_room_by_type(room_type)
        self.__total = room.get_price()* amount * interval.get_night()
        self.__current_booking = Booking(get_current_user().get_firstname(), get_current_user().get_lastname(), self.__current_booking_id, self.__current_hotel, room_type, amount, interval, "Pending")
        new_id = f'{int(self.__current_booking_id) + 1}'
        new_id = '0'*(3 - len(new_id)) + new_id
        self.__current_booking_id = new_id
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content={'room type': room_type,
                                    'checkin_date': interval.get_begin_date().strftime('%A %d %B %Y'),
                                    'checkout_date:': interval.get_end_date().strftime('%A %d %B %Y'),  
                                    'amount': amount,
                                    'summary of charges': self.__total,
                                    'night': interval.get_night()})
    
    def show_coupon_list(self):
        if get_current_user() == None or not isinstance(get_current_user(), Customer):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail={"message": "Please login first"})
        json = {}
        for person in self.__person_list:
            if person.get_firstname() == get_current_user().get_firstname() and person.get_lastname() == get_current_user().get_lastname():
                for coupon in person.get_coupon_list():
                    if coupon.get_exp_date() > date.today():
                        json[f'Coupon #{person.get_coupon_list().index(coupon) + 1}'] = {'Coupon id': coupon.get_coupon_id(),
                                                                                        'Expiration Date': coupon.get_exp_date().strftime('%A %d %B %Y'),
                                                                                        'Amount' : coupon.get_amount()}
                return JSONResponse(status_code = status.HTTP_200_OK,
                            content = json)
        raise HTTPException(statu_code = status.HTTP_200_OK,
                            detail = {'message':'can\'t show coupon'})
    
    def make_early_creditcard_transac(self, arg1, arg2):
        for bank in self.__bank_list:
            for card in bank.get_card_list():
                if card.get_card_id() == arg1 and card.get_cvv() == arg2:   #and credit card cash balance is enough
                    self.__current_transaction = CreditCardTransaction(self.__total, None,  self.__current_transaction_id, "unpaid", arg1, arg2)
                    return 'done'
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = {'message':'no matched card'})

    def make_early_mobilebank_transac(self, arg1, arg2):
        for bank in self.__bank_list:
            if bank.get_name() == arg2:
                for account_id in bank.get_account_id_list(): #and bank account cash balance is enough
                    if account_id == arg1:
                        self.__current_transaction = MobileBankTransaction(self.__total, None, self.__current_transaction_id, "unpaid", arg1, arg2)
                        return 'done'
                raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = {'message':'no matched account'})
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = {'message':'no matched bank'})

    def make_early_paypal_transac(self, arg1, arg2):
        for bank in self.__bank_list:
             for paypal_id in bank.get_paypal_id_list():    #and paypal account cash balance is enough
                if paypal_id == arg1 and arg2 in [person.get_account().get_email() for person in self.__person_list]:      #person.get_account().get_email()
                    self.__current_transaction = PaypalTransaction(self.__total, None, self.__current_transaction_id, "unpaid", arg1, arg2)
                    return 'done'
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = {'message':'no matched account'})

    def select_transaction(self, selection, transaction_arg1, transaction_arg2):#select:str -> paypal, creditcard, mobilebank
        if not isinstance(transaction_arg1, str) or not isinstance(transaction_arg2, str):
            raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                                detail = {'message':'Invalid argument(s) type'})
        if self.__current_booking == None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                detail={"message": "You\'ve not made any booking yet"})
        if selection == 'C':
            self.make_early_creditcard_transac(transaction_arg1, transaction_arg2)
        elif selection == 'M':
            self.make_early_mobilebank_transac(transaction_arg1, transaction_arg2)
        elif selection == 'P':
            self.make_early_paypal_transac(transaction_arg1, transaction_arg2)
        else:
            raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                                detail = {'message':'Invalid selection method'})
        new_id = f'{int(self.__current_transaction_id) + 1}'
        new_id = '0'*(3 - len(new_id)) + new_id
        self.__current_transaction_id = new_id
        self.__current_booking.set_transaction(self.__current_transaction)
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content = {'transaction_type': self.__current_transaction.get_pay_type(),
                                       'transaction_id' : self.__current_transaction.get_id()})

    def select_coupon(self, coupon_id):
        if get_current_user() == None or not isinstance(get_current_user(), Customer):
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                              detail={"message": "Please login first"})
        if self.__current_booking == None or self.__current_transaction == None or self.__current_booking.get_firstname() != get_current_user().get_firstname():
           raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                              detail={"message": "You\'ve not made any transaction yet"})
        if coupon_id == 'None': #User didnot use any coupon
            return JSONResponse(status_code=status.HTTP_200_OK,
                                content={'coupon id': 'None',
                                         'discount amount': 'None',
                                         'current price':self.__current_transaction.get_amount()})
        for coupon in get_current_user().get_coupon_list():
            if coupon.get_coupon_id() == coupon_id and coupon.get_exp_date() > date.today():
                self.__current_transaction.set_amount(self.__current_transaction.get_amount() - coupon.get_amount())
                self.__current_transaction.add_coupon(coupon)
                return JSONResponse(status_code=status.HTTP_200_OK,
                                    content={'coupon id': coupon.get_coupon_id(),
                                             'discount amount': coupon.get_amount(),
                                             'current price':self.__current_transaction.get_amount()})
        return HTTPException(status_code=status.HTTP_200_OK,
                            content={'message':"Invalid coupon_id"})
        
    def credit_card_process(self):
        for bank in self.__bank_list:
            for card in bank.get_card_list():
                if isinstance(self.__current_transaction, CreditCardTransaction) and card.get_card_id() == self.__current_transaction.get_card_id() and card.get_balance() >= self.__current_transaction.get_amount():
                    card.set_balance(card.get_balance() - self.__current_transaction.get_amount())
                    return
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = {'message':'Credit card failed to pay'}) 

    def transaction_process(self):
        if self.__current_booking == None or self.__current_transaction == None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                   detail={"message": "You\'ve not made any transaction yet"})
        if isinstance(self.__current_transaction, CreditCardTransaction):
            self.credit_card_process()  
        self.__current_hotel.set_balance(self.__current_hotel.get_balance() + self.__current_transaction.get_amount())
        self.__current_transaction.set_status("paid")
        self.__current_transaction.set_created_at(date.today())#set date
        self.__current_booking.set_status("arriving")

        self.__current_booking.get_hotel().book_room(self.__current_booking)
        
        get_current_user().add_booking(self.__current_booking)
        if self.__current_transaction.get_coupon_used() != None:
            get_current_user().remove_coupon(self.__current_transaction.get_coupon_used())

        json = {}
        json["Your Booking"] = {'Firstname' : self.__current_booking.get_firstname(),
                                'Lastname' : self.__current_booking.get_lastname(),
                                'Booking number' : self.__current_booking.get_booking_no(),
                                'Hotel' : self.__current_booking.get_hotel().get_name(),
                                'Room Type' : self.__current_booking.get_room_type(),
                                'Room Amount' : self.__current_booking.get_room_quantity(),
                                'Status' : self.__current_booking.get_status(),
                                'Date': {'checkin': self.__current_booking.get_interval().get_begin_date().strftime('%A %d %B %Y'),
                                         'checkout': self.__current_booking.get_interval().get_end_date().strftime('%A %d %B %Y')},
                                'Transaction':{'Transaction Method' : self.__current_transaction.get_pay_type(),
                                              'Transaction number' : self.__current_transaction.get_transaction_id(),
                                              'Transaction amount' : self.__current_transaction.get_amount(),
                                              'Transaction Status' : self.__current_transaction.get_status(),
                                              'Transaction Date' : self.__current_transaction.get_created_at().strftime('%A %d %B %Y')}
                                } 
        
        if isinstance(self.__current_transaction, CreditCardTransaction):
            json["Your Booking"]['Transaction'].update({'Credit Card Number' : self.__current_transaction.get_card_id(),
                                                        'Credit Card CVV' : self.__current_transaction.get_cvv()})

        elif isinstance(self.__current_transaction, MobileBankTransaction):
            json["Your Booking"]['Transaction'].update({'Customer Bank Account ID' : self.__current_transaction.get_account_id(),
                                                        'Customer Bank' : self.__current_transaction.get_bank()})

        elif isinstance(self.__current_transaction, PaypalTransaction):
            json["Your Booking"]['Transaction'].update({'Hotel Email Address' : self.__current_hotel.get_hotel_email(),
                                                        'Customer Email Address' : self.__current_transaction.get_customer_email(),
                                                        'Customer Paypal ID' : self.__current_transaction.get_paypal_id()})
        if self.__current_transaction.get_coupon_used() != None:
            json["Your Booking"]['Transaction'].update({'Coupon used' : {'coupon id': self.__current_transaction.get_coupon_used().get_coupon_id(),
                                                                         'discount amount': self.__current_transaction.get_coupon_used().get_amount()}})
        else:
            json["Your Booking"]['Transaction'].update({'Coupon used' : {'coupon id': 'None',
                                                                         'discount amount': 'None'}})
        self.__current_booking = None
        self.reset_current_cache()

        return JSONResponse(status_code=status.HTTP_200_OK,
                            content = json)
    
    def cancel_booking(self, booking_no, current_user):
        if(current_user == None):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"message": "Please login first"})
        if not isinstance(booking_no, str) or len(booking_no) != 3:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "Invalid booking number"})
        if isinstance(current_user, Customer):
            booking = current_user.search_booking_by_id(booking_no)
            if booking:
                booking.set_status('cancelled')
                booking.get_hotel().cancel_room(booking)
                return JSONResponse(status_code=status.HTTP_200_OK, content={'message':"Cancel booking successfully"})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "No booking_id matched"})

    def add_hotel(self, hotel, current_user):
        if(current_user != None):
            if(current_user.get_account().get_role() == "admin"):
                if isinstance(hotel, Hotel):
                    self.__hotel_list.append(hotel)
                    return JSONResponse(status_code=status.HTTP_200_OK, content={'message':"Add hotel successfully"})
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "Invalid hotel object"})
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"message": "You are not an admin"})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"message": "Please login first"})

    def delete_hotel(self, hotel_name, current_user):
        if(current_user != None):
            if(current_user.get_account().get_role() == "admin"):
                if isinstance(hotel_name, str):
                    for hotel in self.__hotel_list:
                        if(hotel_name == hotel.get_name()):
                            self.__hotel_list.remove(hotel)
                            return JSONResponse(status_code=status.HTTP_200_OK, content={'message':"Delete hotel successfully"})
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "There is no name for this hotel"})
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "Invalid hotel name"})
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"message": "You are not an admin"})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"message": "Please login first"})
 
    def admin_cancel_booking(self, booking_no, current_user):
        if(current_user != None):
            if isinstance(current_user, Admin):
                if isinstance(booking_no, str) and len(booking_no) == 3:
                    for person in self.__person_list:
                        if isinstance(person, Customer):
                            booking = person.search_booking_by_id(booking_no)
                            if booking:
                                booking.get_hotel().cancel_room(booking)
                                booking.set_status("cancelled")
                                return JSONResponse(status_code=status.HTTP_200_OK, content={'message':"Cancel booking successfully"})
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "This booking number does not exist"})
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "Invalid booking number"})
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"message": "You are not an admin"})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"message": "Please login first"})  