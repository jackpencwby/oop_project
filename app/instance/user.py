from ..internal.Customer import Customer
from ..internal.Admin import Admin
from ..internal.Account import Account
from booking import *

admin1_account = Account(email="admin1@gmail.com", password="admin1", role="admin")
admin2_account = Account(email="admin2@gmail.com", password="admin2", role="admin")

customer1_account = Account(email="customer1@gmail.com", password="customer1", role="customer")
customer2_account = Account(email="customer2@gmail.com", password="customer2", role="customer")

admin1 = Admin(firstname="admin", lastname="1", country="Thailand", province="Bangkok", zip_code="10520", birthday="25-11-2004", phone_number="0123456789", account=admin1_account)
admin2 = Admin(firstname="admin", lastname="2", country="Thailand", province="Bangkok", zip_code="10520", birthday="31-12-2004", phone_number="9876543210", account=admin2_account)

customer1 = Customer(firstname="customer", lastname="1", country="Thailand", province="Bangkok", zip_code="10520", birthday="1-1-2005", phone_number="1122334455", account=customer1_account)
customer2 = Customer(firstname="customer", lastname="2", country="Thailand", province="Bangkok", zip_code="10520", birthday="14-2-2005", phone_number="5544332211", account=customer2_account) 

customer1.add_booking(booking1_customer1)
customer1.add_booking(booking2_customer1)

customer2.add_booking(booking1_customer2)
customer2.add_booking(booking2_customer2)