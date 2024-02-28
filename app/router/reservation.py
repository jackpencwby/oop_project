from fastapi import APIRouter
from ..instance.company import company

router = APIRouter(prefix="/reservation", tags=["reservation"], responses={404: {"description": "Not Found"}})

@router.post("/lookupReservation")
async def search_booking(firstname:str, lastname:str, booking_no:str, check_in_date:str):
    company.search_booking(firstname, lastname, booking_no, check_in_date)