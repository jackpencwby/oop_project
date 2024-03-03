from fastapi import APIRouter, HTTPException, status
from ..utils.dependency import get_current_user

router = APIRouter(prefix="/payment", tags=["payment"], responses={404: {"description": "Not Found"}})

@router.post("/")
async def payment(booking_no):
    if(get_current_user() == None):
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail={"message": "Please login first"})
    return get_current_user().payment(booking_no)