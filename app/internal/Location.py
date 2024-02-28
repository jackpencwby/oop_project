class Location:
    def __init__(self, province, district):
        self.__province = province
        self.__district = district

    def get_province(self):
        return self.__province
    
    def get_district(self):
        return self.__district