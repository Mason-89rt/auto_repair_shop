from fastapi import APIRouter
from endpoints.models import Staff_application
from db.DBmanager import base_manager
router = APIRouter()


def post_application(applic: Staff_application):
    res = base_manager.execute("insert into comment_staff(id,staff_id,content) values(?,?,?)", args=(applic.id, applic.staff_id, applic.content))
    return res


@router.post('/new_staff')
def new_application(applic: Staff_application):
    return post_application(applic)