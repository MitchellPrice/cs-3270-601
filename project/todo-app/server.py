from flask import Flask, jsonify, request
from db import TodoDatabase
import time

app = Flask(__name__)

todo_db = TodoDatabase()


@app.route("/todo")
def all_todos():
    show_all = request.args.get('show_all') is not None
    return jsonify(todo_db.list_todos(show_all=show_all))

@app.route("/todo/<todo_id>")
def get_todo(todo_id):
    todo = find_todo(todo_id)
    return jsonify(todo)

@app.route("/todo", methods=["POST"])
def new_todo():
    body = request.json
    todo_db.insert_todo(body['todo'])
    return "OK"

@app.route("/todo/<todo_id>", methods=["PUT"])
def update_todo(todo_id):
    time.sleep(60)
    status = request.args.get('status') 
    if status is None or status == 'completed':
        completed = True
    else:
        completed = False

    todo_db.update_completed(todo_id, completed)
    return "OK"

@app.route("/todo/<todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo_db.delete_todo(todo_id)
    return "OK"

def find_todo(todo_id):
    found_todos = [t for t in todo_db.list_todos(show_all=True) if t[0] == int(todo_id)]
    if len(found_todos) <= 0:
        return None
    else:
        return found_todos[0]

def create_todo(name, description):
    global next_todo_id
    todos.append({
        "id": next_todo_id,
        "name": name,
        "description": description,
    })
    next_todo_id += 1


if __name__ == "__main__":
    app.run()

