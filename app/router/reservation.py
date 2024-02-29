from fastapi import APIRouter
from ..instance.company import company
from ..model.hotel import HotelModel, IntervalModel

router = APIRouter(prefix="/reservation", 
                   tags=["reservation"], 
                   responses={404: {"description": "Not Found"}})

@router.get('/rateListMenu')
async def view_rate(hotel:HotelModel, interval:IntervalModel, amount:int):    #????
    return company.view_rate_from_hotel(hotel, interval, amount)