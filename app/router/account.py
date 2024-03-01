from fastapi import APIRouter
from ..instance.company import company
from ..utils.dependency import get_current_user

router = APIRouter(prefix="/account", tags=["account"], responses={404: {"description": "Not Found"}})

@router.get("/profile")
async def get_personal_information():
    if(get_current_user() == None):
        return "Error"
    return get_current_user().get_personal_information()

@router.get("/MyReservations")
async def get_my_travelling():
    if(get_current_user() == None):
        return "Error"
    return get_current_user().get_my_travelling()






