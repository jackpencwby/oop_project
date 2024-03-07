from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from datetime import date
from .Customer import Customer
from .Account import Account
from .Interval import Interval 
from .Booking import Booking
from .Opinion import Opinion
from .Bank import Bank
from .CreditCardTransaction import CreditCardTransaction
from .MobileBankTransaction import MobileBankTransaction
from .PaypalTransaction import PaypalTransaction
from ..utils.dependency import set_current_user
from ..utils.dependency import get_current_user

class Company:
    def __init__(self, name):
        self.__name = name
        self.__person_list = []
        self.__hotel_list = []
        self.__bank_list = []
        self.__total = 0
        self.__current_hotel = None
        self.__current_booking = None
        self.__current_booking_id = "001"
        self.__current_transaction = None
        self.__current_transaction_id = "001"

    def get_name(self):
        return self.__name
    
    def get_person_list(self):
        return self.__person_list
    
    def get_hotel_list(self):
        return self.__hotel_list
    
    def add_person(self, person):
        # Validation
        self.__person_list.append(person)

    def add_hotel(self, hotel):
        # Validation
        self.__hotel_list.append(hotel)

    def add_bank(self,bank):
        if isinstance(bank,Bank):
            self.__bank_list.append(bank)
            return "Bank Adding success in list"
        return "Bank Adding error in list"

    def login(self, email, password):
        for person in self.__person_list:
            if email == person.get_account().get_email():
                if password == person.get_account().get_password():
                    set_current_user(person)
                    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Login Successfully"})
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"message": "Wrong Password"})
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"message": "Email doesn't exist"})
    
    def register(self, firstname, lastname, country, province, zip_code, birthday, phone_number, email, password, confirm_password): 
        for person in self.__person_list:
            if email == person.get_account().get_email():
                return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "Email already exist"})
        if password == confirm_password:
            account = Account(email, password, role="customer")
            customer = Customer(firstname, lastname, country, province, zip_code, birthday, phone_number, account)
            self.__person_list.append(customer)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Register Successfully"})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "Password doesn't match"})
    
    def search_nearby_hotel(self, country, province):
        nearby_hotel_list = []
        for hotel in self.__hotel_list:
            if hotel.get_location().get_country() == country or hotel.get_location().get_province() == province:
                nearby_hotel_list.append({"hotel_name": hotel.get_name(),
                                          "location": {"country": hotel.get_location().get_country(), "province": hotel.get_location().get_province()}})
        return nearby_hotel_list

    def search_booking(self, firstname, lastname, booking_no, check_in_date):
        for person in self.__person_list:
            if(person.get_account().get_role() == "customer"):  
                if(firstname == person.get_firstname() and lastname == person.get_lastname()):
                    for booking in person.get_booking_list():
                        if(booking_no == booking.get_booking_no() and check_in_date == booking.get_interval().get_begin_date()):
                            return {"firstname": booking.get_firstname(), 
                                    "lastname": booking.get_lastname(),
                                    "booking_no": booking.get_booking_no(),
                                    "hotel": {"hotel_name": booking.get_hotel().get_name(),
                                                "location": {"country": booking.get_hotel().get_location().get_country(), 
                                                            "province": booking.get_hotel().get_location().get_province()}},
                                    "room_type": booking.get_room_type(),
                                    "room_quantity": booking.get_room_quantity(),
                                    "check_in_date": booking.get_interval().get_begin_date(),
                                    "check_out_date": booking.get_interval().get_end_date(),
                                    "status": booking.get_status()}
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "No booking Information"})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "Firstname and Surname doesn't exist"})
    
    def get_personal_information(self, current_user):
        if(current_user == None):
            return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail={"message": "Please login first"})
        return JSONResponse(status_code=status.HTTP_200_OK, content={"firstname": current_user.get_firstname(),
                "lastname": current_user.get_lastname(),
                "email": current_user.get_account().get_email(),
                "country": current_user.get_country(),
                "province": current_user.get_province(),
                "zip_code": current_user.get_zip_code(),
                "birthday": current_user.get_birthday(),
                "phone_number": current_user.get_phone_number()})
    
    def get_my_travelling(self, current_user):
        if(current_user == None):
            return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail={"message": "Please login first"})
        arriving = []
        cancelled = []
        for booking in current_user.get_booking_list():
            if(booking.get_status() == "paid"):
                arriving.append({"firstname": booking.get_firstname(),
                                 "lastname": booking.get_lastname(),
                                 "booking_no": booking.get_booking_no(),
                                 "hotel": {"hotel_name": booking.get_hotel().get_name(),
                                           "location": {"country": booking.get_hotel().get_location().get_country(), 
                                                        "province": booking.get_hotel().get_location().get_province()}},
                                 "room_type": booking.get_room_type(),
                                 "room_quantity": booking.get_room_quantity(),
                                 "check_in_date": booking.get_interval().get_begin_date(),
                                 "check_out_date": booking.get_interval().get_end_date()})
            elif(booking.get_status() == "cancel"):
                cancelled.append({"firstname": booking.get_firstname(),
                                 "lastname": booking.get_lastname(),
                                 "booking_no": booking.get_booking_no(),
                                 "hotel": {"hotel_name": booking.get_hotel().get_name(),
                                           "location": {"country": booking.get_hotel().get_location().get_country(), 
                                                        "province": booking.get_hotel().get_location().get_province()}},
                                 "room_type": booking.get_room_type(),
                                 "room_quantity": booking.get_room_quantity(),
                                 "check_in_date": booking.get_interval().get_begin_date(),
                                 "check_out_date": booking.get_interval().get_end_date()})
        return JSONResponse(status_code=status.HTTP_200_OK, content={"arriving": arriving, "cancelled": cancelled})

    def get_my_favorite_hotel(self, current_user):
        if(current_user == None):
            return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail={"message": "Please login first"})
        my_favorite_hotel = []
        for hotel in current_user.get_my_favorite_hotel_list():
            my_favorite_hotel.append({"hotel_name": hotel.get_name(),
                                      "location": {"country": hotel.get_location().get_country(), "province": hotel.get_location().get_province()}})
        return JSONResponse(status_code=status.HTTP_200_OK, content=my_favorite_hotel)
    
    def add_favorite_hotel(self, hotel_name, current_user):
        if(current_user == None):
            return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail={"message": "Please login first"})
        for hotel in self.__hotel_list:
            if(hotel_name == hotel.get_name()):
                current_user.add_favorite_hotel(hotel)
                return JSONResponse(status_code=status.HTTP_200_OK, content="Add Successfully")
    
    def add_opinion(self, hotel_name, rating, comment, current_user):
        if(current_user == None):
            return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail={"message": "Please login first"})
        if 0 > rating > 5:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "Invalid rating"})
        for hotel in self.__hotel_list:
            if hotel.get_name() == hotel_name:
                hotel.add_opinion(Opinion(rating, comment))
                return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Add opinion successfully"})
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "Hotel not found"})
    
    def get_opinion(self, hotel_name):
        for hotel in self.__hotel_list:
            if hotel_name == hotel.get_name():
                if len(hotel.get_opinion()) == 0:
                    return JSONResponse(status_code=status.HTTP_200_OK, content={"rating": "No rating",
                                                                             "comment": "No comment"})
                else: return JSONResponse(status_code=status.HTTP_200_OK, content={"rating": sum([int(opinion.get_rating()) for opinion in hotel.get_opinion()]) / len(hotel.get_opinion()),
                                                                             "comment": [opinion.get_comment() for opinion in hotel.get_opinion()]})
            
    def view_rate_from_hotel(self, hotel_name, date_list, amount):
        needed_hotel, interval = self.convert_hotel_and_interval(hotel_name, date_list)
        room_list = needed_hotel.get_available_room(interval, amount)
        json = {}
        for room in room_list:
            json[f'{room.get_type()} room type'] = {'price per night': room.get_price(),
                                                    'image': 'jpeg'}
        if len(json) == 0:
            return {'error': 'no room available'}
        return json

    def convert_hotel_and_interval(self, hotel_name, date_list):
        needed_hotel = None
        for hotel in self.__hotel_list:
            if hotel.get_name() == hotel_name:
                needed_hotel = hotel
                break
        if needed_hotel == None:
            raise Exception('Error')
        by, bm, bd = [int(x) for x in date_list[0].split('-')]
        ey, em, ed = [int(x) for x in  date_list[1].split('-')] 
        begin = date(by, bm, bd)
        end = date(ey, em, ed)
        if begin > date.today() and end > date.today() and end > begin:
            interval = Interval(begin = begin, end = end)
            return [needed_hotel, interval]
        raise Exception('Invalid Date')
    
    def select_room(self, hotel_name, date_list, amount, room_type):
        if get_current_user() == None:
            return {'response':'please login first.'}
        self.__current_hotel, interval = self.convert_hotel_and_interval(hotel_name, date_list)
        self.__current_hotel.select_room(interval, amount, room_type)
        room = self.__current_hotel.get_room_by_type(room_type)
        self.__total = room.get_price()* amount * interval.get_night()

        self.__current_booking = Booking(get_current_user().get_firstname(), get_current_user().get_lastname(), self.__current_booking_id, self.__current_hotel, room_type, amount, interval, "Pending")
        
        # run current booking id by 1
        new_id = f'00{int(self.__current_booking_id) + 1}'
        self.__current_booking_id = new_id

        return {'room type': room_type,
                'checkin_date': interval.get_begin_date(),
                'checkout_date:': interval.get_end_date(),  
                'amount': amount,
                'summary of charges': self.__total,
                'night': interval.get_night()}

    # def continue_to_payment(self):
    #     pass

    ##Yew
    def show_coupon_list(self):
        json = {}
        for person in self.__person_list:
            if person.get_firstname() == get_current_user().get_firstname() and person.get_lastname() == get_current_user().get_lastname():
                for coupon in person.get_coupon_list():
                    json[f'Coupon #{person.get_coupon_list().index(coupon) + 1}'] = {'Coupon id': coupon.get_coupon_id(),
                                                                                    'Expiration Date': coupon.get_exp_date(),
                                                                                    'Amount' : coupon.get_amount()}
        return json
    
    def select_transaction(self, selection, transaction_arg1, transaction_arg2):#select:str -> paypal, creditcard, mobilebank
        ### First Section ###
        loopcount = False
        for person in self.__person_list:
            if person.get_firstname() == self.__current_booking.get_firstname() and person.get_lastname() == self.__current_booking.get_lastname():
                for bank in self.__bank_list:
                    if selection == 'C': #CreditCard transaction 
                        for card in bank.get_card_list():
                            if card.get_card_id() == transaction_arg1 and card.get_cvv() == transaction_arg2:
                                self.__current_transaction = CreditCardTransaction(self.__total,None,self.__current_transaction_id,"Unpaid",transaction_arg1,transaction_arg2)
                                loopcount = True
                                break
                   
                    elif selection == 'M': #MobileBank transaction
                        for account_id in bank.get_account_id_list():
                            if account_id == transaction_arg1 and bank.get_name() == transaction_arg2:
                                self.__current_transaction = MobileBankTransaction(self.__total,None,self.__current_transaction_id,"Unpaid",transaction_arg1,transaction_arg2)
                                loopcount = True
                                break
        
                    elif selection == 'P': #Paypal transaction
                        for paypal_id in bank.get_paypal_id_list():
                            if paypal_id == transaction_arg1 and person.get_account().get_email() == transaction_arg2:
                                self.__current_transaction = PaypalTransaction(self.__total,None,self.__current_transaction_id,"Unpaid",transaction_arg1,transaction_arg2)
                                loopcount = True
                                break
    
        if loopcount == False: #Argument or search cannot found
           raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": "Invalid Transaction argument or Transaction argument not found in System"})
        
        #run current transaction id by 1
        new_id = f'00{int(self.__current_transaction_id) + 1}'
        self.__current_transaction_id = new_id

        self.__current_booking.set_transaction(self.__current_transaction)
        
        if loopcount == True:
            return "Transaction Method Selection successed"
        else:
            return "Transaction Method Selection Failed"
        
    def select_coupon(self,coupon_id):
        ### Second Section ###
        for coupon in get_current_user().get_coupon_list():
            if coupon.get_coupon_id() == coupon_id and coupon.get_exp_date() > str(date.today()):
                self.__current_transaction.set_amount(self.__current_transaction.get_amount() - coupon.get_amount())
                get_current_user().get_coupon_list().pop(get_current_user().get_coupon_list().index(coupon))#delete coupon from list in customer
                return "Coupon Selection successed"
        return "Coupon selection failed"
        
    def transaction_process(self):
        for bank in self.__bank_list:
            for card in bank.get_card_list():
                if isinstance(self.__current_transaction,CreditCardTransaction):
                    if card.get_balance() >= self.__total:
                        card.set_balance(card.get_balance() - self.__total)
          
        ### Last Section ###
        self.__current_hotel.set_balance(self.__current_hotel.get_balance() + self.__total)#Increase hotel balance amount
        self.__current_transaction.set_status("Paid")

        self.__current_transaction.set_created_at(str(date.today()))#set date
        self.__current_booking.set_status("Wait_for_checkin")

        get_current_user().add_booking(self.__current_booking)

        json = {}
        json["Your Booking"] =      {'Firstname' : self.__current_booking.get_firstname(),
                                    'Lastname' : self.__current_booking.get_lastname(),
                                    'Booking number' : self.__current_booking.get_booking_no(),
                                    'Hotel' : self.__current_booking.get_hotel().get_name(),
                                    'Room Type' : self.__current_booking.get_room_type(),
                                    'Room Amount' : self.__current_booking.get_room_quantity(),
                                    'Status' : self.__current_booking.get_status(),
                                    'Transaction Method' : self.__current_transaction.get_paytype(),
                                    'Transaction number' : self.__current_transaction.get_transaction_id(),
                                    'Transaction amount' : self.__current_transaction.get_amount(),
                                    'Transaction Status' : self.__current_transaction.get_status(),
                                    'Transaction Date' : self.__current_transaction.get_created_at()}
                    
        if isinstance(self.__current_booking.get_transaction(),CreditCardTransaction):
            json["Your Booking"].update({'Credit Card Number' : self.__current_transaction.get_card_id(),
                                        'Credit Card CVV' : self.__current_transaction.get_cvv()})

        elif isinstance(self.__current_booking.get_transaction(),MobileBankTransaction):
            json["Your Booking"].update({'Customer Bank Account ID' : self.__current_transaction.get_account_id(),
                                        'Customer Bank' : self.__current_transaction.get_bank()})

        elif isinstance(self.__current_booking.get_transaction(),PaypalTransaction):
            json["Your Booking"].update({'Hotel Email Address' : self.__current_hotel.get_hotel_email(),
                                        'Customer Email Address' : self.__current_transaction.get_customer_email(),
                                        'Customer Paypal ID' : self.__current_transaction.get_paypal_id()})
        
        #remove current attribute
        self.__current_booking = None
        self.__current_transaction = None
        self.__current_hotel = None

        return json