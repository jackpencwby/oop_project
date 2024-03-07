from fastapi import APIRouter, HTTPException, status
from ..instance.company import company
from ..utils.dependency import get_current_user

router = APIRouter(prefix="/search", tags=["search"], responses={404: {"description": "Not Found"}})

@router.post("/hotel")
async def search_nearby_hotel(data: dict) -> dict:
    country = data["country"]
    province = data["province"]
    all_hotel = company.search_nearby_hotel(country, province)
    return {"all_hotel": all_hotel}

@router.post("/reservation")
async def search_booking(data: dict) -> dict:
    firstname = data["firstname"]
    lastname = data["lastname"]
    booking_no = data["booking_no"]
    check_in_date = data["check_in_date"]
    reservation =  company.search_booking(firstname, lastname, booking_no, check_in_date)
    return {"reservation": reservation}
