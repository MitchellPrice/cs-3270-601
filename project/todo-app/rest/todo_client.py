import requests


class TodoClient:
    def __init__(self, url='http://localhost:5000'):
        self.__url = url

    def insert_todo(self, todo):
        body = { 'todo': todo }
        requests.post('{}/todo'.format(self.__url), json=body)

    def list_todos(self, show_all=False):
        results = requests.get('{}/todo'.format(self.__url))
        return results.json()

    def update_completed(self, todo_id, completed=True):
        requests.put('{}/todo/{}'.format(self.__url, todo_id))
        
    def delete_todo(self, todo_id):
        requests.delete('{}/todo/{}'.format(self.__url, todo_id))


