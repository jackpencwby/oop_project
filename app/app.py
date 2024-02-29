from fastapi import FastAPI
from .router import search
from .router import reservation
from .router import auth
from .instance.user import *

app = FastAPI()

app.include_router(search.router)
app.include_router(reservation.router)
app.include_router(auth.router)


