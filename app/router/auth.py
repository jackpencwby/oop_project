from fastapi import APIRouter
from datetime import datetime
from pydantic import EmailStr
from ..instance.company import company


router = APIRouter(prefix="/auth", tags=["auth"], responses={404: {"description": "Not Found"}})

@router.post("/register")
async def register(firstname:str, lastname:str, country:str, province:str, zip_code:str, birthday:str, phone_number:str, email:EmailStr, password:str, confirm_password:str):
    return company.register(firstname, lastname, country, province, zip_code, birthday, phone_number, email, password, confirm_password)

@router.post("/login")
async def login(email:EmailStr, password:str):
    return company.login(email, password)
    


