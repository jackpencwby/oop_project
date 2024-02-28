from ..internal.Booking import Booking
from ..internal.Interval import Interval

booking1_customer1 = Booking(firstname="customer", 
                             lastname="1", 
                             booking_no="001", 
                             room_type="small", 
                             room_quantity="1", 
                             interval=Interval(begin="1-1-2024", end="2-1-2024"),
                             status="paid")

booking2_customer1 = Booking(firstname="customer", 
                             lastname="1", 
                             booking_no="002", 
                             room_type="medium", 
                             room_quantity="2", 
                             interval=Interval(begin="29-1-2024", end="31-1-2024"), 
                             status="pending")

booking1_customer2 = Booking(firstname="customer", 
                             lastname="2", 
                             booking_no="003", 
                             room_type="large", 
                             room_quantity="3", 
                             interval=Interval(begin="14-2-2024", end="17-2-2024"),
                             status="cancel")

booking2_customer2 = Booking(firstname="customer", 
                             lastname="2", 
                             booking_no="004", 
                             room_type="small", 
                             room_quantity="4", 
                             interval=Interval(begin="1-3-2024", end="7-3-2024"), 
                             status="paid")

