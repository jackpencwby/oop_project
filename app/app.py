from fastapi import FastAPI
from .router import home
from .router import search
from .router import auth
from .router import account
from .router import hotel
from .router import reservation
from .router import payment
from .router import admin

app = FastAPI()

app.include_router(home.router)
app.include_router(search.router)
app.include_router(auth.router)
app.include_router(account.router)
app.include_router(hotel.router)
app.include_router(reservation.router)
app.include_router(payment.router)
app.include_router(admin.router)



