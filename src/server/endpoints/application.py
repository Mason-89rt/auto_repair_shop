from fastapi import APIRouter
from endpoints.models import application, Put
from db.DBmanager import base_manager
router = APIRouter()


def get_application_id(id: int):
    res = base_manager.execute("SELECT * FROM application WHERE id=?", args=(id,), many=False)
    return application(id=res[0], client_id=res[1], description=res[2],status=res[3], comment_staff_id=res[4])


def get_application():
    res = base_manager.execute("select * from application", args=(), many=True)
    applic = []
    for us in res:
        applic.append(application(id=us[0], client_id=us[1], description=us[2],status=us[3], comment_staff_id=us[4]))
    return res


def post_application(applic: application):
    res = base_manager.execute("insert into application(id,client_id,description,status,comment_staff_id) values(?,?,?,?,?)", args=(applic.id, applic.client_id, applic.description, applic.status, applic.comment_staff_id))
    return res


@router.put('/{id}')
def put_application(id: int, app: Put):
    res = base_manager.execute("UPDATE application SET status=?,description=?,comment_staff_id=? WHERE id=?", (app.description,app.status,app.comment_staff_id, id))
    return res


def delete_application(id: int):
    res = base_manager.execute("delete from application where id=?", args=(id,))
    return res


# Endpoints
@router.get('/application/{id}')
def get_application_endpoint(id: int):
    return get_application_id(id)


@router.get('/applications')
def get_application_endpoint():
    return get_application()


@router.post('/new_application')
def new_application(applic: application):
    return post_application(applic)



@router.delete('/application/{id}')
def delete_application_id(id: int):
    return delete_application(id)
