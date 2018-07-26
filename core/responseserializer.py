from flask_restful import fields

todolist_fields = {
    'todolist_id': fields.Integer,
    'title': fields.String,
    'items': fields.String,
    'created_date': fields.DateTime(dt_format='rfc822'),
    'modified_date': fields.DateTime(dt_format='rfc822'),
}


class TodoList(object):
    def __init__(self, id, title, items, createdDate, modifiedDate):
        self.id = id
        self.title = title
        self.items = items
        self.created_date = createdDate
        self.modified_date = modifiedDate
