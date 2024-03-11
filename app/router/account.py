from fastapi import APIRouter, HTTPException, status
from ..instance.company import company
from ..utils.dependency import get_current_user

router = APIRouter(prefix="/account", tags=["account"], responses={404: {"description": "Not Found"}})

@router.get("/profile")     #กู
async def get_personal_information():
    return company.get_personal_information(get_current_user())

@router.get("/MyReservations")
async def get_my_travelling():
    return company.get_my_travelling(get_current_user())

@router.get("/MyFavoriteHotel")
async def get_my_favorite_hotel():
    return company.get_my_favorite_hotel(get_current_user())

@router.post('/CancelBooking')
async def cancel_booking(data:dict):
    return company.cancel_booking(data['booking_no'], get_current_user())

@router.post("/AddFavoriteHotel")
async def add_my_favorite_hotel(data:dict):
    return company.add_favorite_hotel(data['hotel_name'], get_current_user())

@router.post("/UnFavoriteHotel")
async def add_my_favorite_hotel(data:dict):
    return company.remove_favorite_hotel(data['hotel_name'], get_current_user())

@router.post("/AddOpinion")
async def add_opinion(data:dict):
    return company.add_opinion(data['hotel_name'], data['rating'], data['comment'], get_current_user())






