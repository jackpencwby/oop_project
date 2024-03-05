from fastapi import APIRouter, HTTPException, status
from ..instance.company import company

router = APIRouter(prefix="/hotel", tags=["hotel"], responses={404: {"description": "Not Found"}})

@router.get("/opinion")
async def get_opinion(hotel_name):
    return company.get_opinion(hotel_name)


