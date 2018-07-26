from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TodoList(db.Model):
    id = db.Column('todolist_id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(200), nullable=False)
    createdDate = db.Column('created_date', db.DateTime, nullable=False)
    lastModified = db.Column('last_modified_date', db.DateTime, nullable=False)
    items = db.Column('items', db.JSON, nullable=False)
    modifiedDate = db.relationship('ModifiedDate', backref='todolist')

    def __init__(self, title, lastModfied, items):
        self.createdDate = title
        self.lastModified = lastModfied
        self.items = items

    def __repr__(self):
        return '<TodoList %r>' % self.title


class ModifiedDate(db.Model):
    id = db.Column('modified_date_id', db.Integer, primary_key=True)
    modifiedDate = db.Column('modified_date', db.DateTime, nullable=False)
    todolistId = db.Column('todolist_id', db.ForeignKey('todo_list.todolist_id'), nullable=False)

    def __init__(self, modifiedDate):
        self.modifiedDate = modifiedDate

    def __repr__(self):
        return '<ModifiedDate %r>' % self.id
