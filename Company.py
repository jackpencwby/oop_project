class Company:
    def __init__(self, name):
        self.__name = name
        self.__account_list = []
        self.__hotel_list = []

    def get_name(self):
        return self.__name
    
    def get_account_list(self):
        return self.__account_list
    
    def get_hotel_list(self):
        return self.__hotel_list
    
    def add_account_list(self, account):
        # Validation
        self.__account_list.append(account)

    def add_hotel_list(self, hotel):
        # Validation
        self.__hotel_list.append(hotel)

    def register(self):
        pass

    def login(self):
        pass

    # def search_nearby_hotel(self):
    #     pass

    def search_booking(self):
        pass