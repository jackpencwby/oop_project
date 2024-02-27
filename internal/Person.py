class Person:
    def __init__(self, firstname, lastname, country, province, zip_code, birthday, phone_number, account):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__country = country
        self.__province = province
        self.__zip_code = zip_code
        self.__birthday = birthday
        self.__phone_number = phone_number
        self.__account = account
    
    def get_firstname(self):
        return self.__firstname
    
    def get_lastname(self):
        return self.__lastname
    
    def get_country(self):
        return self.__country
    
    def get_province(self):
        return self.__country
    
    def get_zip_code(self):
        return self.__zip_code
    
    def get_birthday(self):
        return self.__birthday
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_account(self):
        return self.__account
        

    