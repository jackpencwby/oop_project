from fastapi import HTTPException, status

class Room:
    def __init__(self, room_no, type, price):
        self.__room_no = room_no
        self.__type = type
        self.__price = price
        self.__reserved_interval = []
        self.__pending_interval = []
    
    def get_room_no(self):
        return self.__room_no
    
    def get_type(self):
        return self.__type
    
    def get_price(self):
        return self.__price

    def is_available_at(self, interval): #check both reserved, pending 
        if self.is_pending_at(interval) or self.is_reserved_at(interval):
            return False
        return True
    
    def is_pending_at(self, interval): 
        checkin = interval.get_begin_date()
        checkout = interval.get_end_date()
        for room_interval in self.__pending_interval:
            reserved_checkin = room_interval.get_begin_date()
            reserved_checkout = room_interval.get_end_date()
            if (checkin >= reserved_checkin and checkin <= reserved_checkout) or (checkout >= reserved_checkin and checkout <= reserved_checkout):
                return True
        return False
    
    def is_reserved_at(self, interval):   
        checkin = interval.get_begin_date()
        checkout = interval.get_end_date()
        for room_interval in self.__reserved_interval:
            reserved_checkin = room_interval.get_begin_date()
            reserved_checkout = room_interval.get_end_date()
            if (checkin >= reserved_checkin and checkin <= reserved_checkout) or (checkout >= reserved_checkin and checkout <= reserved_checkout):
                return True
        return False

    def add_pending_interval(self, interval): 
        self.__pending_interval.append(interval)
        return
    
    def move_pending_to_reserved(self, interval):
        if interval in self.__pending_interval:
            self.__pending_interval.remove(interval)
            self.__reserved_interval.append(interval)
            return 
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail={'message':'failed to reserve'})
    
    def remove_reserved_or_pending(self, interval):
        if self.is_reserved_at(interval):
            self.__reserved_interval.remove(interval)
            return 
        if self.is_pending_at(interval):
            self.__pending_interval.remove(interval)
            return 
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail={'message':'failed to remove reserved'})
    

    