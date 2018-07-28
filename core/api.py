from flask import Blueprint
from flask import request
from flask_restful import Resource, Api
from flask_restful import reqparse, marshal_with

from dao.operation import *

from core.responseserializer import todolist_fields
from core.requestparser import TodoListWithIdParser, TodoListParser

core_blueprint = Blueprint('core', __name__)
apiserver = Api(core_blueprint)


def abort_on_non_exist():
    """
    Check Existance of a resource, terminate request when resource does not exist
    :return:
    """
    pass


class TodoList(Resource):
    """
    Use model column for serialization of todolist
    """

    @marshal_with(todolist_fields, envelope='data')
    def get(self):
        """
        Get all todolists or get by id
        :return:
        """
        useremail = request.headers.get('Useremail')
        data = get_todolists(useremail)
        return data, 200

    def post(self):
        """
        Create new todolist
        :return:
        """
        args = TodoListParser.parse_args()
        useremail = request.headers.get('Useremail')
        title = args['title']
        items = args['items']
        create_todolist({'title': title, 'useremail': useremail, 'items': items})
        return 'Created', 201


class TodoListWithId(Resource):
    @marshal_with(todolist_fields, envelope='data')
    def get(self, todolist_id):
        """
        Get Todolist with certain Id
        :param todolist_id:
        :return:
        """
        data = get_todolist(todolist_id)
        return data, 200

    def delete(self, todolist_id):
        """
        Delete todolist accouding todolist id
        :return:
        """
        todolist_id = todolist_id
        delete_todolist(todolist_id)
        return 'Deleted', 204

    def put(self, todolist_id):
        """
        Update todolist
        :return:
        """
        args = TodoListWithIdParser.parse_args()
        title = args['title']
        items = args['items']
        update_todolist(todolist_id, {'title': title, 'items': items})
        return 'Updated', 202


apiserver.add_resource(TodoList, '/todolists')
apiserver.add_resource(TodoListWithId, '/todolists/<int:todolist_id>')
