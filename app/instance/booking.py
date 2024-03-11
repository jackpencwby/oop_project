from ..internal.Booking import Booking
from ..internal.Interval import Interval
from ..internal.Transaction import Transaction
from ..internal.CreditCardTransaction import CreditCardTransaction
from ..internal.MobileBankTransaction import MobileBankTransaction
from ..internal.PaypalTransaction import PaypalTransaction
from .hotel import *
from datetime import date

booking1_customer1 = Booking(firstname="customer", 
                             lastname="1", 
                             booking_no="001",
                             hotel=hotel1, 
                             room_type="small", 
                             room_quantity=1, 
                             interval=Interval(begin=date(2024, 1, 1), end=date(2024, 1, 2)),
                             status="passed",
                             transaction=CreditCardTransaction(amount=1000,
                                                               created_at=date(2023, 12, 1),
                                                               transaction_id='001',
                                                               status='Paid',
                                                               card_id='30100',
                                                               cvv='400'
                                                               ))

booking2_customer1 = Booking(firstname="customer", 
                             lastname="1", 
                             booking_no="002",
                             hotel=hotel2, 
                             room_type="medium", 
                             room_quantity=2, 
                             interval=Interval(begin=date(2024, 1, 29), end=date(2024, 1, 31)), 
                             status="passed",
                             transaction=CreditCardTransaction(amount=12000,
                                                               created_at=date(2023, 12, 1),
                                                               transaction_id='002',
                                                               status='Paid',
                                                               card_id='30100',
                                                               cvv='400'
                                                               ))

booking3_customer1 = Booking(firstname="customer", 
                             lastname="1", 
                             booking_no="003",
                             hotel=hotel3, 
                             room_type="large", 
                             room_quantity=1, 
                             interval=Interval(begin=date(2024, 1, 29), end=date(2024, 1, 31)), 
                             status="cancelled",
                             transaction=None)

booking1_customer2 = Booking(firstname="customer", 
                             lastname="2", 
                             booking_no="004",
                             hotel=hotel4, 
                             room_type="small", 
                             room_quantity=1, 
                             interval=Interval(begin=date(2024, 4, 2), end=date(2024, 4, 4)),
                             status="arriving",
                             transaction=PaypalTransaction(amount=8000,
                                                           created_at=date(2024, 2, 1),
                                                           transaction_id='004',
                                                           status='Paid',
                                                           customer_email='customer2@gmail.com',
                                                           paypal_id='5001000'
                                                           ))

booking2_customer2 = Booking(firstname="customer", 
                             lastname="2", 
                             booking_no="005",
                             hotel=hotel5, 
                             room_type="medium", 
                             room_quantity=2, 
                             interval=Interval(begin=date(2024, 1, 30), end=date(2024, 2, 2)), 
                             status="passed",
                             transaction=PaypalTransaction(amount=45000,
                                                          created_at=date(2024, 1, 29),
                                                          transaction_id='005',
                                                          status='Paid',
                                                          customer_email='customer2@gmail.com',
                                                          paypal_id='5001000'
                                                          ))

booking3_customer2 = Booking(firstname="customer", 
                             lastname="2", 
                             booking_no="006",
                             hotel=hotel6, 
                             room_type="large", 
                             room_quantity=1, 
                             interval=Interval(begin=date(2024, 1, 15), end=date(2024, 2, 19)), 
                             status="cancelled",
                             transaction=PaypalTransaction(amount=12000,
                                                          created_at=date(2024, 1, 12),
                                                          transaction_id='006',
                                                          status='cancelled',
                                                          customer_email='customer2@gmail.com',
                                                          paypal_id='5001000'
                                                          ))
