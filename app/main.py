from fastapi import FastAPI
import models
from routes import router_city
from routes_user import router_user
from config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_city, prefix="/city", tags=["city"])
app.include_router(router_user, prefix="/user", tags=["user"])
