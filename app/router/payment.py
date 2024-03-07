from fastapi import APIRouter, HTTPException, status
from ..utils.dependency import get_current_user
from ..instance.company import company

router = APIRouter(prefix="/payment", tags=["payment"], responses={404: {"description": "Not Found"}})

#@router.post("/")
#search transaction from booking no method?
#async def payment(booking_no):
    #if(get_current_user() == None):
        #raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail={"message": "Please login first"})
    #return get_current_user().search_transaction(booking_no)  

@router.get("/showcoupon")
async def show_coupon():
    return company.show_coupon_list()
    
@router.post("/methodselect")
async def methodselect(selection:str,transaction_arg1:str,transaction_arg2:str):
    return company.select_transaction(selection,transaction_arg1,transaction_arg2)

@router.post("/couponselect")
async def couponselect(coupon_id:str):
    return company.select_coupon(coupon_id)

@router.post("/process")
async def process():
    return company.transaction_process()

    


