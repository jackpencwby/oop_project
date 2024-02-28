from fastapi import FastAPI
from .router import reservation

app = FastAPI()

app.include_router(reservation.router)

