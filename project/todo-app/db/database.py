import sqlite3
import os


class TodoDatabase:
    def __init__(self, file_name='todo.db'):
        self.__file_name = file_name
        self.__conn = None
        self.__initialize()
        print(self.list_todos())

    def __initialize(self):
        if self.__conn is not None:
            raise Exception("Can't initialize database with open connection")

        database_exists = os.path.exists(self.__file_name)
        self.__conn = sqlite3.connect(self.__file_name)
        if not database_exists:
            self.__setup_database()

    def __setup_database(self):
        print('Setup database')
        self.__execute('CREATE TABLE Todo (id INTEGER PRIMARY KEY AUTOINCREMENT, todo TEXT, completed INT DEFAULT 0)')
        self.__insert_sample_data()

    def __insert_sample_data(self):
        todos = ('Finish this',
                 'Go home',
                 'Eat something')

        for t in todos:
            self.insert_todo(t)

    def insert_todo(self, todo):
        print('Inserting todo: {}'.format(todo))
        return tuple(self.__execute('INSERT INTO Todo (todo) VALUES (?)', todo))

    def list_todos(self, show_all=False):
        if show_all:
            command = 'SELECT id, todo, completed FROM Todo'
        else:
            command = 'SELECT id, todo, completed FROM Todo WHERE completed = 0'
        return tuple(self.__execute(command))

    def update_completed(self, todo_id, completed=True):
        self.__execute('UPDATE Todo SET completed = ? WHERE id = ?', int(completed), todo_id)
        
    def delete_todo(self, todo_id):
        self.__execut('DELETE FROM Todo WHERE id = ?', int(todo_id))

    def __execute(self, command, *args):
        cur = self.__conn.cursor()
        result = cur.execute(command, args)
        self.__conn.commit()
        return result








