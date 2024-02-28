from Room import Room
from Opinion import Opinion

class Hotel:
    def __init__(self, name, location, room_list):
        self.__name = name
        self.__location = location
        self.__status = None
        self.__room_list = room_list

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

    def get_available_room(self, interval, amount):
        type_amount = {'small':0, 'medium':0, 'large':0}
        example = []
        for room in self.__room_list:
            if room.is_available_at(interval):
                type_amount[room.get_type()] += 1
                if room.get_type() not in [room.get_type() for room in example]:
                    example.append(room)
        return example
    
    def get_opinion(self):
        return self.__opinion_list

    def append_opinion(self, comment, rating):
        self.__opinion_list.append(Opinion(comment, rating))
                
                


    
    