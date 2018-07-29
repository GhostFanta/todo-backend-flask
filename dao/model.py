from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import json


db = SQLAlchemy()


def dump_datetime(value):
    if value is None:
        return None
    return value.strftime("%Y-%m-%d %H:%M:%S")


class TodoList(db.Model):
    id = db.Column('todolist_id', db.Integer, primary_key=True)
    useremail = db.Column('useremail', db.String(200), nullable=False)
    title = db.Column('title', db.String(200), nullable=False)
    createdDate = db.Column('created_date', db.DateTime, nullable=False)
    lastModified = db.Column('last_modified_date', db.DateTime, onupdate=datetime.utcnow(), nullable=False)
    items = db.Column('items', db.JSON, nullable=False)
    modifiedDate = db.relationship('ModifiedDate', backref='todolist')

    def __init__(self, title, useremail, createdDate, lastModfied, items):
        self.title = title
        self.useremail = useremail
        self.createdDate = createdDate
        self.lastModified = lastModfied
        self.items = items

    @property
    def serialize(self):
        """
        Return json serialized data for the consumption of front-end
        :return:
        """
        return {
            'id': self.id,
            'useremail': self.useremail,
            'title': self.title,
            'createdtime': dump_datetime(self.createdDate),
            'lastmodifiedtime': dump_datetime(self.lastModified),
            'items': json.loads(self.items),
        }

    def __repr__(self):
        return '<TodoList %r>' % self.title


class ModifiedDate(db.Model):
    id = db.Column('modified_date_id', db.Integer, primary_key=True)
    modifiedDate = db.Column('modified_date', db.DateTime, nullable=False)
    todolistId = db.Column('todolist_id', db.ForeignKey('todo_list.todolist_id'), nullable=False)

    def __init__(self, todolistId, modifiedDate):
        self.todolistId = todolistId
        self.modifiedDate = modifiedDate

    @property
    def serialize(self):
        return {
            'todolistid': self.todolistId,
            'modifieddate': self.modifiedDate
        }

    def __repr__(self):
        return '<ModifiedDate %r>' % self.id
