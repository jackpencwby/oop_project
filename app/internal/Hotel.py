from .Room import Room
from .Opinion import Opinion

class Hotel:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__status = None
        self.__room_list = []

    def get_name(self):
        return self.__name
    
    def get_location(self):
        return self.__location
    
    def get_status(self):
        return self.__status
    
    def change_status(self, status):
        # Validation
        self.__status = status

    def get_room_list(self):
        return self.__room_list
    
    def add_room(self, room):
        # Validation
        self.__room_list.append(room)

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
    
    # def select_room(self, interval, room_type, amount):
    #     for room in self.__room_list:
    #         if room.get_type() == room_type:
    #             amount -= 1
    #             room.add_pending_interval(interval)
    #         if amount == 0:
    #             return 'done'


    def get_opinion(self):
        return self.__opinion_list

    def append_opinion(self, comment, rating):
        self.__opinion_list.append(Opinion(comment, rating))
                
                


    
    