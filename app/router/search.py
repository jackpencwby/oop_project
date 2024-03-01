from fastapi import APIRouter
from ..instance.company import company
from ..utils.dependency import get_current_user

router = APIRouter(prefix="/search", tags=["search"], responses={404: {"description": "Not Found"}})

@router.get("/FindHotel")
async def go_to_hotel_page():
    pass

@router.get("/FindReservation")
async def go_to_reservation_page():
    pass

@router.get("/AllHotel")
async def search_nearby_hotel(country: str, province: str):
    return company.search_nearby_hotel(country, province)

@router.get("/Reservation")
async def search_booking(firstname: str, lastname: str, booking_no: str, check_in_date: str):
    return company.search_booking(firstname, lastname, booking_no, check_in_date)




