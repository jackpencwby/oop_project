from .Person import Person

class Admin(Person):
    def __init__(self, firstname, lastname, country, province, zip_code, birthday, phone_number, account):
        super().__init__(firstname, lastname, country, province, zip_code, birthday, phone_number, account)

    # def add_hotel(self):
    #     pass

    # def delete_hotel(self):
    #     pass

    # def edit_hotel_name(self):
    #     pass

    # def edit_hotel_status(self):
    #     pass

    # def edit_room_status(self):
    #     pass

    # def edit_small_room_price(self):
    #     pass

    # def edit_medium_room_price(self):
    #     pass

    # def edit_large_room_price(self):
    #     pass

    # def force_cancel_booking(self):
    #     pass