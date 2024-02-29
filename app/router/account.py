from fastapi import APIRouter
from ..internal.Customer import Customer


router = APIRouter(prefix="/account", tags=["account"], responses={404: {"description": "Not Found"}})

@router.get("/profile")
async def get_personal_information():
    pass