from fastapi import FastAPI
import models
from routes import router_city
from routes_user import router_user
from routes_softskill import router_softskill
from routes_hardskill import router_hardskill
from routes_formation import router_formation
from routes_experience import router_experience
from routes_company import router_company
from routes_application import router_application
from routes_joboffer import router_joboffer
from routes_status import router_status
from routes_user_hardskill import router_user_hardskill
from routes_user_softskill import router_user_softskill
from config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_city, prefix="/city", tags=["city"])
app.include_router(router_user, prefix="/user", tags=["user"])
app.include_router(router_softskill, prefix="/softskill", tags=["softskill"])
app.include_router(router_hardskill, prefix="/hardskill", tags=["hardskill"])
app.include_router(router_formation, prefix="/formation", tags=["formation"])
app.include_router(router_experience, prefix="/experience",
                   tags=["experience"])
app.include_router(router_company, prefix="/company", tags=["company"])
app.include_router(router_joboffer, prefix="/joboffer", tags=["joboffer"])
app.include_router(router_application,
                   prefix="/application", tags=["application"])
app.include_router(router_status, prefix="/status", tags=["status"])
app.include_router(router_user_hardskill,
                   prefix="/user_hardskill", tags=["user_hardskill"])
app.include_router(router_user_softskill,
                   prefix="/user_softskill", tags=["user_softskill"])
