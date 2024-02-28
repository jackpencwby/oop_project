from fastapi import APIRouter

router = APIRouter(prefix="/search", tags=["search"], responses={404: {"description": "Not Found"}})






