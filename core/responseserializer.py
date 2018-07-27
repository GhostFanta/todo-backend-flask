from flask_restful import fields

todolist_fields = {
    'id': fields.Integer,
    'useremail': fields.String,
    'title': fields.String,
    'items': fields.String,
    'createdDate': fields.DateTime(dt_format='rfc822'),
    'lastModified': fields.DateTime(dt_format='rfc822'),
}


class TodoList(object):
    def __init__(self, id, useremail, title, items, createdDate, lastModifiedDate):
        self.id = id
        self.useremail = useremail
        self.title = title
        self.items = items
        self.created_date = createdDate
        self.last_modified_date = lastModifiedDate
