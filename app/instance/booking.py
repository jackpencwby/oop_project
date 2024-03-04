from ..internal.Booking import Booking
from ..internal.Interval import Interval
from .hotel import *

booking1_customer1 = Booking(firstname="customer", 
                             lastname="1", 
                             booking_no="001",
                             hotel=hotel1, 
                             room_type="small", 
                             room_quantity="1", 
                             interval=Interval(begin="1-1-2024", end="2-1-2024"),
                             status="pending")

booking2_customer1 = Booking(firstname="customer", 
                             lastname="1", 
                             booking_no="002",
                             hotel=hotel2, 
                             room_type="medium", 
                             room_quantity="2", 
                             interval=Interval(begin="29-1-2024", end="31-1-2024"), 
                             status="paid")

booking3_customer1 = Booking(firstname="customer", 
                             lastname="1", 
                             booking_no="003",
                             hotel=hotel3, 
                             room_type="large", 
                             room_quantity="3", 
                             interval=Interval(begin="14-2-2024", end="17-2-2024"), 
                             status="cnacel")

booking1_customer2 = Booking(firstname="customer", 
                             lastname="2", 
                             booking_no="004",
                             hotel=hotel4, 
                             room_type="small", 
                             room_quantity="1", 
                             interval=Interval(begin="2-1-2024", end="4-1-2024"),
                             status="pending")

booking2_customer2 = Booking(firstname="customer", 
                             lastname="2", 
                             booking_no="005",
                             hotel=hotel5, 
                             room_type="medium", 
                             room_quantity="2", 
                             interval=Interval(begin="30-1-2024", end="2-2-2024"), 
                             status="paid")

booking3_customer2 = Booking(firstname="customer", 
                             lastname="2", 
                             booking_no="006",
                             hotel=hotel6, 
                             room_type="large", 
                             room_quantity="3", 
                             interval=Interval(begin="15-1-2024", end="19-2-2024"), 
                             status="cancle")

