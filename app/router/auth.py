from fastapi import APIRouter
from pydantic import EmailStr
from ..instance.company import company
from ..utils.dependency import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"], responses={404: {"description": "Not Found"}})

@router.post("/register")
async def register(data:dict):
    firstname = data["firstname"]
    lastname = data["lastname"]
    country = data["country"]
    province = data["province"]
    zip_code = data["zip_code"]
    birthday = data["birthday"]
    phone_number = data["phone_number"]
    email = data["email"]
    password = data["password"]
    confirm_password = data["confirm_password"]
    return company.register(firstname, lastname, country, province, zip_code, birthday, phone_number, email, password, confirm_password)

@router.post("/login")
async def login(dict: dict):
    email = dict["email"]
    password = dict["password"]
    return company.login(email, password)

@router.put("/logout")
async def logout():
    return company.logout(get_current_user())
