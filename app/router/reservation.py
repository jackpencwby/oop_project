from fastapi import APIRouter
from ..instance.company import company

router = APIRouter(prefix="/reservation", tags=["reservation"], responses={404: {"description": "Not Found"}})

@router.post('/rateListMenu')
async def view_rate(data: dict):  #hotel_name:str, checkin:str, checkout:str, amount:int
    return company.view_rate_from_hotel(data['hotel_name'], [data['checkin'], data['checkout']], data['amount']) #change to classroom example

@router.post('/reviewDetails') #if logged in, it will show pay method, else show 'continue' and login first then go guestInfo
async def select(data: dict): #hotel_name:str, checkin:str, checkout:str, amount:int, room_type:str
    return company.select_room(data['hotel_name'], [data['checkin'], data['checkout']], data['amount'], data['room_type'])
    #return 'pls login first' or 'detail info'



