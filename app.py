from flask import Flask
from flask import request
from service import ToDoService
import requests

app = Flask(__name__)
todo_service = ToDoService()


@app.route('/')
def hello_world():
    return 'Hello WorldZZZ!'


@app.route('/todo', methods=["POST"])
def create_todo():
    result = todo_service.create(request.get_json())
    return result.to_json()


@app.route('/do-todo/<todo_id>')
def do_todo(todo_id):
    result = todo_service.mark_as_done(todo_id)
    return result.to_json()


@app.route('/get-all')
def get_all():
    return todo_service.get_all_undone()


if __name__ == '__main__':
    app.run(debug=True)
