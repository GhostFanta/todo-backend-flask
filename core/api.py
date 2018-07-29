from flask import Blueprint
from flask import request
from flask_restful import Resource, Api
from flask_restful import abort, marshal_with
import json

from dao.operation import *

from core.requestparser import TodoListWithIdParser, TodoListParser

core_blueprint = Blueprint('core', __name__)
apiserver = Api(core_blueprint)


def abort_on_non_exist(todolist_id):
    abort(404, message="Todolist {} does not exist".format(todolist_id))


class TodoList(Resource):
    """
    Use model column for serialization of todolist
    """

    def get(self):
        """
        Get all todolists or get by id
        :return:
        """
        useremail = request.headers.get('Useremail')
        data = get_todolists(useremail)
        return [item.serialize for item in data]

    def post(self):
        """
        Create new todolist, remember to return serialized data.
        :return:
        """
        # useremail = request.headers.get('Useremail')
        args = TodoListParser.parse_args()
        useremail = request.headers.get('Useremail')
        title = args['title']
        items = args['todoitems']
        print(title)
        print(items)
        val = create_todolist({'title': title,
                               'useremail': useremail,
                               'items': items})
        return val.serialize, 201


class TodoListWithId(Resource):
    def get(self, todolist_id):
        """
        Get Todolist with certain Id
        :param todolist_id:
        :return:
        """
        data = get_todolist(todolist_id)
        return data.serialize, 200

    def delete(self, todolist_id):
        """
        Delete todolist accouding todolist id
        :return:
        """
        try:
            todolist_id = todolist_id
            delete_todolist(todolist_id)
            return 'Deleted', 204
        except Exception:
            abort_on_non_exist(todolist_id)

    def put(self, todolist_id):
        """
        Update todolist
        :return:
        """
        try:
            args = TodoListWithIdParser.parse_args()
            title = args['title']
            items = args['items']
            update_todolist(todolist_id, {'title': title, 'items': items})
            return 'Updated', 202
        except Exception:
            abort_on_non_exist(todolist_id)


apiserver.add_resource(TodoList, '/todolists')
apiserver.add_resource(TodoListWithId, '/todolists/<int:todolist_id>')
