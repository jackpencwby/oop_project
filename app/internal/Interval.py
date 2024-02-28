class Interval:
    def __init__(self, begin, end) -> None:
        self.__begin_datetime = begin
        self.__end_datetime = end

    def get_begin_datetime(self):
        return self.__begin_datetime

    def get_end_date_time(self):
        return self.__end_datetime

    def is_intersect_to(self, interval):
        return True