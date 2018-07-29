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


def abort_on_operation_failed(err):
    abort(500, message="Operation Failed: {}".format(err))


class TodoList(Resource):
    """
    Use model column for serialization of todolist
    """

    def get(self):
        """
        Get all todolists or get by id
        :return:
        """
        try:
            useremail = request.headers.get('Useremail')
            data = get_todolists(useremail)
            for i in data:
                print(i)
            return [item.serialize for item in data], 200
        except Exception:
            abort_on_operation_failed(Exception)

    def post(self):
        """
        Create new todolist, remember to return serialized data.
        :return:
        """
        try:
            args = TodoListParser.parse_args()
            useremail = request.headers.get('Useremail')
            title = args['title']
            items = args['items']
            val = create_todolist({'title': title,
                                   'useremail': useremail,
                                   'items': items})
            return val.serialize, 201
        except Exception:
            abort_on_operation_failed(Exception)


class TodoListWithId(Resource):
    def get(self, todolist_id):
        """
        Get Todolist with certain Id
        :param todolist_id:
        :return:
        """
        data = get_todolist(todolist_id)
        print(data)
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
            # TODO: For some reason the parser is not parsing what I want, I have more
            # than one items in items field but parser parse me only one. Give up debugging
            # due to time limit.
            title = request.json['title']
            items = request.json['items']
            updated_todolist = update_todolist(todolist_id,
                                               {'title': title, 'items': json.dumps(items).replace("'", '\\"')})
            return updated_todolist.serialize, 202

        except Exception:
            abort_on_non_exist(todolist_id)


apiserver.add_resource(TodoList, '/todolists')
apiserver.add_resource(TodoListWithId, '/todolists/<int:todolist_id>')
