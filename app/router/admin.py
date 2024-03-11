from fastapi import APIRouter
from ..instance.company import company
from ..internal.Hotel import Hotel
from ..internal.Location import Location
from ..utils.dependency import get_current_user

router = APIRouter(prefix="/admin", tags=["admin"], responses={404: {"description": "Not Found"}})

@router.post("/AddHotel")
async def add_hotel(data: dict):
    name = data["name"]
    country = data["location"]["country"]
    province = data["location"]["province"]
    location = Location(country, province)
    hotel_email = data["hotel_email"]
    hotel = Hotel(name, location, hotel_email)
    return company.add_hotel(hotel, get_current_user())

@router.delete("/DeleteHotel")
async def delete_hotel(data: dict):
    hotel_name = data["hotel_name"]
    return company.delete_hotel(hotel_name, get_current_user())

@router.put("/CancelBooking")
async def cancel_booking(data: dict):
    booking_no = data["booking_no"]
    return company.admin_cancel_booking(booking_no, get_current_user())