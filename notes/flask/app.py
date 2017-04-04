from flask import Flask, jsonify
app = Flask(__name__)

next_todo_id=1
todos = [{
        "id": 0,
        "name": "My Todo",
        "description": "Here is something for you to do",
}]

@app.route("/todo")
def all_todos():
    return jsonify(todos)

@app.route("/todo/<todo_id>")
def get_todo(todo_id):
    todo = find_todo(todo_id)
    return jsonify(todo)

@app.route("/todo", methods=["POST"])
def new_todo():
    create_todo("Post", "Post created me")
    return "OK"

@app.route("/todo/<todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = find_todo(todo_id)
    todo['description'] = 'updated'
    return jsonify(todo)

@app.route("/todo/<todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = find_todo(todo_id)
    if todo is None:
        return "OK"
    todos.remove(todo)
    return "OK"

def find_todo(todo_id):
    found_todos = [t for t in todos if t['id'] == int(todo_id)]
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
    create_todo('first', 'This one')
    create_todo('second', 'This other one')
    create_todo('third', 'final one')
    app.run()

