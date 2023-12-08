from pydantic import BaseModel


class User(BaseModel):
    id: int
    login: str
    password: str


class User_login(BaseModel):
    login: str


class User_logins_password(BaseModel):
    login: str
    password: str


class Staff(BaseModel):
    id: int
    name: str
    surname: str
    post_id: int
    user_id: int


class Staff_name_surname(BaseModel):
    name: str
    surname: str

class application(BaseModel):
    id: int
    client_id: int
    description: str
    status: str
    comment_staff_id: int


class Put(BaseModel):
    description: str
    status: str
    comment_staff_id: int


class Staff_application(BaseModel):
    id: int
    staff_id: int
    content: str