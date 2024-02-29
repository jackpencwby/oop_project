from datetime import date as Date

# class Date:
#     def __init__(self) -> None:
#         year
#         month
#         day
#     def < > ==  -

class Interval:
    def __init__(self, begin, end):
        self.__begin_datetime = begin   #Date object
        self.__end_datetime = end       #Date object

    def get_begin_date(self):
        return self.__begin_datetime

    def get_end_date(self):
        return self.__end_datetime