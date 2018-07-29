from flask_restful import reqparse

TodoListParser = reqparse.RequestParser()
TodoListParser.add_argument('title', type=str, location='form')
TodoListParser.add_argument('items', type=str, location='form')

TodoListWithIdParser = reqparse.RequestParser()
TodoListWithIdParser.add_argument('title', type=str, location='form')
TodoListWithIdParser.add_argument('items', type=str, location='form')