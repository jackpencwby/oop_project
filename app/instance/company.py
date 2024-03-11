from ..internal.Company import Company
from .hotel import *
from .user import *
from .bank import *

company = Company(name="marriot", hotel_list = [hotel1, hotel2, hotel3, hotel4, hotel5, hotel6])

company.add_person(admin1)
company.add_person(admin2)
company.add_person(customer1)
company.add_person(customer2)

company.add_bank(scb)
company.add_bank(kbank)


