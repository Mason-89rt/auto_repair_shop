import requests


def get_all_applications():
    response = requests.get('http://127.0.0.1:8000/application_start/applications')
    post_data = response.json()
    return post_data


#get_all_applications()


#def get_all_application():
#    id_application = input("enter the ID of the application you want to receive")
#    response = requests.get(f'http://127.0.0.1:8000/application_start/application/{id_application}')
#    post_data = response.json()
#    print(post_data)
#
#
#get_all_application()
#
#
#def post_application():
#    id_application = input("ID")
#    client_id = input("client_id")
#    description = input("description")
#    status = input("status")
#    comment_staff_id = input("comment_staff_id")
#    data = {"id": id_application,
#            "client_id": client_id,
#            "description": description,
#            "status": status,
#            "comment_staff_id": comment_staff_id}
#    response = requests.post('http://127.0.0.1:8000/application_start/new_application', json=data)
#    print(response.json())
#
#
#post_application()
#
#
#def update_application():
#    id_application = input("enter the ID of the application you want to update")
#    description = input("description")
#    status = input("status")
#    data = {'description': description,
#            'status': status}
#    response = requests.put(f'http://127.0.0.1:8000/application_start/{id_application}', json=data)
#    new_post_data = response.json()
#    print(new_post_data)
#
#
#update_application()
#
#
#def delete_id_application():
#    id_application = input("enter the ID of the application you want to delete")
#    response = requests.delete(f'http://127.0.0.1:8000/application_start/application/{id_application}')
#    post_data = response.json()
#    print(post_data)
#
#
#delete_id_application()