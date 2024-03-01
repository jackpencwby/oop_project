from ..internal.Company import Company
from .hotel import *
from .user import *

company = Company(name="marriot")

company.add_person(admin1)
company.add_person(admin2)
company.add_person(customer1)
company.add_person(customer2)

company.add_hotel(hotel1)
company.add_hotel(hotel2)
company.add_hotel(hotel3)
company.add_hotel(hotel4)
company.add_hotel(hotel5)
company.add_hotel(hotel6)

