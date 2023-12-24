from fastapi import FastAPI
from db.DBmanager import base_manager
from set import SCRIPTS_PATH
from endpoints.user import router as router_users
from endpoints.application import router as router_application
from endpoints.Staff_application import router as router_staff_application
app = FastAPI()
app.include_router(router_application, prefix='/application_start')
app.include_router(router_staff_application, prefix='/tt')
app.include_router(router_users, prefix='/users_start')
base_manager.cr_base(SCRIPTS_PATH)
