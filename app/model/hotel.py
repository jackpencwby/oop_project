from pydantic import BaseModel
from datetime import date as Date
from ..internal.Location import Location
from ..internal.Interval import Interval

class HotelModel(BaseModel):
    name: str
    location: str
    status: None
    room_list: list
    
class IntervalModel(BaseModel):
    begin: Date
    end: Date