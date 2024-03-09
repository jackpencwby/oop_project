from fastapi import APIRouter
from ..instance.company import company
from ..utils.dependency import get_current_user

router = APIRouter(prefix="/admin", tags=["admin"], responses={404: {"description": "Not Found"}})

@router.post("/AddHotel")
async def add_hotel(hotel):
    return company.admin_add_hotel(hotel, get_current_user())

@router.delete("/DeleteHotel")
async def delete_hotel(hotel_name):
    return company.admin_delete_hotel(hotel_name, get_current_user())

@router.put("/CancelBooking")
async def cancel_booking(booking_no):
    return company.admin_cancel_booking(booking_no, get_current_user())