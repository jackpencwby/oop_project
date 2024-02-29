class Location:
    def __init__(self, country, province):
        self.__country = country
        self.__province = province

    def get_country(self):
        return self.__country

    def get_province(self):
        return self.__province