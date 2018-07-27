from flask import Blueprint
from flask import jsonify
from flask_restful import Resource, Api
from flask_restful import abort, reqparse, fields, marshal_with

from dao.operation import *

from core.responseserializer import todolist_fields

from helper.sqlhelper import *

core_blueprint = Blueprint('core', __name__)
apiserver = Api(core_blueprint)


def abort_on_non_exist(todolist_id, item):
    if item is 'null':
        abort(404, message="Todolist {} doesn't exist".format(todolist_id))


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
        data = get_todolists()
        return data

    def post(self):
        """
        Create new todolist
        :return:
        """
        # args = parser.parse.args()
        return 'Created', 201


class TodoListWithId(Resource):
    @marshal_with(todolist_fields, envelope='data')
    def get(self, todolist_id):
        """

        :param todolist_id:
        :return:
        """
        data = get_todolist(todolist_id)
        return data

    def delete(self, todolist_id):
        """
        Delete todolist accouding todolist id
        :return:
        """
        delete_todolist(todolist_id)
        return '', 204

    def put(self, todolist_id):
        """
        Update todolist
        :return:
        """
        todolist = ''
        return todolist, 201


apiserver.add_resource(TodoList, '/todolists')
apiserver.add_resource(TodoListWithId, '/todolists/<int:todolist_id>')
