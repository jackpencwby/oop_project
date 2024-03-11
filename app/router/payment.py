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
async def methodselect(data:dict):
    return company.select_transaction(data['selection'], data['transaction_arg1'], data['transaction_arg2'])

@router.post("/couponselect")
async def couponselect(data:dict):
    return company.select_coupon(data['coupon_id'])

@router.get("/process")
async def process():
    return company.transaction_process()

    


