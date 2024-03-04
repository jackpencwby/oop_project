from .Room import Room
from .Opinion import Opinion

class Hotel:
    def __init__(self, name, location, hotel_email, balance=0):
        self.__name = name
        self.__location = location
        self.__hotel_email = hotel_email
        self.__balance = balance
        self.__status = None
        self.__room_list = []

    #Request จากคนทำ payment ขอเพิ่ม attribute hotel_email ของโรงแรมเพือนำไปแสดงใน paypaltransaction
    #Request จากคนทำ payment ขอเพิ่ม attribute balance ของโรงแรมเพือเก็บจำนวนเงินทั้งหมดที่ได้จากลูกค้า
    #from flukky ถ้ามันได้ใช้ก็ใส่ได้เลยขรั่บ

    def get_name(self):
        return self.__name
    
    def get_location(self):
        return self.__location

    def get_hotel_email(self):
        return self.__hotel_email
    
    def get_status(self):
        return self.__status

    def get_balance(self):
        return self.__balance
    
    def change_status(self, status):
        # Validation
        self.__status = status

    def get_room_list(self):
        return self.__room_list
    
    def add_room(self, room):
        # Validation
        self.__room_list.append(room)

    def set_balance(self,balance):
        if isinstance(balance,int):
            self.__balance = balance
            return  "Hotel balance setting success"
        return  "Hotel balance setting error"
        
    def get_available_room(self, interval, amount):     #Fluk
        all_available_room = []
        type_amount = {'small':0, 'medium':0, 'large':0}
        for room in self.__room_list:
            if room.is_available_at(interval):
                type_amount[room.get_type()] += 1
                all_available_room.append(room)
        available_room = []
        for k, v in type_amount.items():
            if v >= amount:      
                for room in all_available_room:
                    if room.get_type() == k:
                        available_room.append(room) 
                        break
        return available_room
    
    def select_room(self, interval, amount, room_type):     #fluk
        for room in self.__room_list:
            if room.get_type() == room_type and room.is_available_at(interval):
                amount -= 1
                room.add_pending_interval(interval)
            if amount == 0:
                return 'done'

    def get_room_by_type(self, type):
        for room in self.__room_list:
            if room.get_type() == type:
                return room

    def get_opinion(self):
        return self.__opinion_list

    def append_opinion(self, comment, rating):
        self.__opinion_list.append(Opinion(comment, rating))
                
                


    
    