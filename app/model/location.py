from pydantic import BaseModel

class LocationModel(BaseModel):
    country: str
    province: str