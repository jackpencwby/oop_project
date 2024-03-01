from fastapi import FastAPI
from .router import home
from .router import search
from .router import auth
from .router import account
# from .router import reservation

app = FastAPI()

app.include_router(home.router)
app.include_router(search.router)
app.include_router(auth.router)
app.include_router(account.router)
# app.include_router(reservation.router)




