from fastapi import APIRouter, HTTPException, status
from ..instance.company import company
from ..utils.dependency import get_current_user

router = APIRouter(prefix="/account", tags=["account"], responses={404: {"description": "Not Found"}})

@router.get("/profile")
async def get_personal_information():
    return company.get_personal_information(get_current_user())

@router.get("/MyReservations")
async def get_my_travelling():
    return company.get_my_travelling(get_current_user())

@router.get("/MyFavoriteHotel")
async def get_my_favorite_hotel():
    return company.get_my_favorite_hotel(get_current_user())






