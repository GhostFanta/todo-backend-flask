from flask_restful import reqparse

TodoListParser = reqparse.RequestParser()
TodoListParser.add_argument('title', type=str)
TodoListParser.add_argument('items', type=str)

TodoListWithIdParser = reqparse.RequestParser()
TodoListWithIdParser.add_argument('title', type=str)
TodoListWithIdParser.add_argument('items', type=str)
