import os.path
import pickle


class ToDoModel:
    def __init__(self, todo_id, name, description, created_on, due_date):
        self.id = todo_id
        self.name = name
        self.description = description
        self.created_on = created_on
        self.due_date = due_date
        self.is_done = False

    def to_json(self):
        return {'id': self.id, 'name': self.name, 'description': self.description, 'created_on': self.created_on,
                'due_date': self.due_date, 'is_done': self.is_done}


class ToDoDB:
    _file_to_save = 'local_db.pkl'
    _current_last_id = 0

    def __init__(self):
        if os.path.exists(ToDoDB._file_to_save):
            with open(ToDoDB._file_to_save, "rb") as f:
                self.todos = pickle.load(f)
            if len(self.todos) != 0:
                ToDoDB._current_last_id = len(self.todos)
        else:
            self.todos = []

    def create(self, name, description, created_on, due_date):
        new_id = ToDoDB._current_last_id + 1
        ToDoDB._current_last_id += 1
        todo = ToDoModel(new_id, name, description, created_on, due_date)
        self.todos.append(todo)
        ToDoDB._dump_db(self)
        return todo

    def mark_as_done(self, todo_id):
        todo_id_int = int(todo_id)
        self.todos[todo_id_int].is_done = True
        ToDoDB._dump_db(self)
        return self.todos[todo_id_int]

    def _dump_db(self):
        with open(ToDoDB._file_to_save, "wb") as f:
            pickle.dump(self.todos, f)

    def get_all_undone(self):
        undone_todos = []
        for todo in self.todos:
            if not todo.is_done:
                undone_todos.append(todo)
        return undone_todos
