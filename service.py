from models import ToDoDB
from datetime import datetime, timedelta, date
import collections
import json


class ToDoService:
    def __init__(self):
        self.db = ToDoDB()

    def create(self, params):
        datetime_obj = datetime.now()
        current_date = datetime_obj.date()
        if 'due_date' not in params:
            week = timedelta(7)
            due_date = current_date + week
        else:
            # DD-MM-YYYY
            due_date_param = params['due_date']
            due_date_param_obj = str.split(due_date_param, '-')
            due_date = date(int(due_date_param_obj[0]), int(due_date_param_obj[1]), int(due_date_param_obj[2]))
        return self.db.create(params['name'], params['description'], current_date, due_date)

    def mark_as_done(self, todo_id):
        return self.db.mark_as_done(todo_id)

    def get_all_undone(self):
        todos = self.db.get_all_undone()
        all_todos = {}
        for todo in todos:
            all_todos[todo.id] = (todo.to_json())
        # d = collections.defaultdict(dict)
        # for todo in all_todos:
        #     d[todo[0]][todo[1]] = todo[2]

        return all_todos
