from ..internal.Booking import Booking
from ..internal.Interval import Interval
from .hotel import *
from datetime import date

booking1_customer1 = Booking(firstname="customer", 
                             lastname="1", 
                             booking_no="001",
                             hotel=hotel1, 
                             room_type="small", 
                             room_quantity=1, 
                             interval=Interval(begin=date(2024, 1, 1), end=date(2024, 1, 2)),
                             status="pending")

booking2_customer1 = Booking(firstname="customer", 
                             lastname="1", 
                             booking_no="002",
                             hotel=hotel2, 
                             room_type="medium", 
                             room_quantity=2, 
                             interval=Interval(begin=date(2024, 1, 29), end=date(2024, 1, 31)), 
                             status="paid")

booking3_customer1 = Booking(firstname="customer", 
                             lastname="1", 
                             booking_no="003",
                             hotel=hotel3, 
                             room_type="large", 
                             room_quantity=3, 
                             interval=Interval(begin=date(2024, 1, 14), end=date(2024, 1, 31)), 
                             status="cancelled")

booking1_customer2 = Booking(firstname="customer", 
                             lastname="2", 
                             booking_no="004",
                             hotel=hotel4, 
                             room_type="small", 
                             room_quantity=1, 
                             interval=Interval(begin=date(2024, 1, 2), end=date(2024, 1, 4)),
                             status="pending")

booking2_customer2 = Booking(firstname="customer", 
                             lastname="2", 
                             booking_no="005",
                             hotel=hotel5, 
                             room_type="medium", 
                             room_quantity=2, 
                             interval=Interval(begin=date(2024, 1, 30), end=date(2024, 2, 2)), 
                             status="paid")

booking3_customer2 = Booking(firstname="customer", 
                             lastname="2", 
                             booking_no="006",
                             hotel=hotel6, 
                             room_type="large", 
                             room_quantity=3, 
                             interval=Interval(begin=date(2024, 1, 15), end=date(2024, 2, 19)), 
                             status="cancelled")

