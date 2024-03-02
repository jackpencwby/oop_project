from pydantic import BaseModel
from .location import LocationModel

class HotelModel(BaseModel):
    name: str
    location: LocationModel
