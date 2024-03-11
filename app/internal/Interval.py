from datetime import date

class Interval:
    def __init__(self, begin:date, end:date):
        self.__begin_date = begin   #Date object
        self.__end_date = end       #Date object

    def get_begin_date(self):
        return self.__begin_date

    def get_end_date(self):
        return self.__end_date
    
    def get_night(self):
        return (self.__end_date - self.__begin_date).days