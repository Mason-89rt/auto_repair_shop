import requests


def get_login_user(login):
    data = {"login": login}
    response = requests.get('http://127.0.0.1:8000/users_start/users_login', json=data)
    post_data = response.json()
    return post_data
#
#
def get_login_password_user(login, password):
    data = {"login": login, "password": password}
    response = requests.get('http://127.0.0.1:8000/users_start/users_login_password', json=data)
    post_data = response.json()
    return post_data
#
#
def get_all_user():
    response = requests.get('http://127.0.0.1:8000/users_start/users')
    post_data = response.json()
    return post_data
#
#
#get_all_user()
#
#
#def get_id_user(user_id):
#    response = requests.get(f'http://127.0.0.1:8000/users_start/users/{user_id}')
#
#    if response.status_code == 200:
#        return response.json()
#    else:
#        return None
#
#
def post_user(login, password):
    data = {"login": login, "password": password}
    response = requests.post('http://127.0.0.1:8000/users_start/new_user', json=data)
    return response
#
#
#post_user()


#def update_user():
#    id_user = input("enter the ID of the user you want to update")
#    login = input("Login")
#    data = {'login': login}
#    response = requests.put(f'http://127.0.0.1:8000/users_start/user_login/{id_user}', json=data)
#    new_post_data = response.json()
#    print(new_post_data)
#
#
#update_user()
#
#def delete_user():
#    id_user = input("enter the ID of the user you want to delete")
#    response = requests.delete(f'http://127.0.0.1:8000/users_start/user/{id_user}')
#    new_post_data = response.json()
#    print(new_post_data)
#
#
#delete_user()
