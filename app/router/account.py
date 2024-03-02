from fastapi import APIRouter, HTTPException, status
from ..instance.company import company
from ..utils.dependency import get_current_user

router = APIRouter(prefix="/account", tags=["account"], responses={404: {"description": "Not Found"}})

@router.get("/profile")
async def get_personal_information():
    if(get_current_user() == None):
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail={"message": "Please login first"})
    return get_current_user().get_personal_information()

@router.get("/MyReservations")
async def get_my_travelling():
    if(get_current_user() == None):
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail={"message": "Please login first"})
    return get_current_user().get_my_travelling()

@router.get("/MyFavoriteHotel")
async def get_my_favorite_hotel():
    if(get_current_user() == None):
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail={"message": "Please login first"})
    return get_current_user().get_my_favorite_hotel()






