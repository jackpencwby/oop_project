from fastapi import FastAPI
from .router import reservation
from .instance.user import *

app = FastAPI()

app.include_router(reservation.router)



