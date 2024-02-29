from fastapi import APIRouter
from ..instance.company import company
from ..internal.Location import Location

router = APIRouter(prefix="/search", tags=["search"], responses={404: {"description": "Not Found"}})

@router.post("/lookupReservation")
async def search_booking(firstname:str, lastname:str, booking_no:str, check_in_date:str):
    return company.search_booking(firstname, lastname, booking_no, check_in_date)
