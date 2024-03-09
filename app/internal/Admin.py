from .Person import Person

class Admin(Person):
    def __init__(self, firstname, lastname, country, province, zip_code, birthday, phone_number, account):
        super().__init__(firstname, lastname, country, province, zip_code, birthday, phone_number, account)

    # def add_hotel(self):
    #     pass

    # def delete_hotel(self):
    #     pass

    # def force_cancel_booking(self):
    #     pass