from fastapi import APIRouter
from ..instance.company import company

router = APIRouter(prefix="/hotel", tags=["hotel"], responses={404: {"description": "Not Found"}})

@router.post("/opinion")
async def get_opinion(data:dict):
    return company.get_opinion(data['hotel_name'])


