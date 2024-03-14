from fastapi import APIRouter
from ..instance.company import company

router = APIRouter(prefix="/payment", tags=["payment"], responses={404: {"description": "Not Found"}})

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

    


