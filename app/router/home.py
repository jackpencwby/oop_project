from fastapi import APIRouter

router = APIRouter(prefix="/home", tags=["home"], responses={404: {"description": "Not Found"}})

# @router.get('/')
# async def get_home_page():
#     pass
