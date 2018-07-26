from flask import Blueprint
from flask_restful import Resource, Api

from flask import jsonify

core_blueprint = Blueprint('core', __name__)
apiserver = Api(core_blueprint)


class TodoList(Resource):
    def get(self):
        """
        Get all todolists or get by id
        :return:
        """
        pass

    def post(self):
        """
        Create new todolist
        :return:
        """
        pass

    def delete(self):
        """
        Delete todolist accouding todolist id
        :return:
        """
        pass

    def put(self):
        """

        :return:
        """
        pass

    def patch(self):
        """

        :return:
        """
        pass


apiserver.add_resource(TodoList, '/todolist')