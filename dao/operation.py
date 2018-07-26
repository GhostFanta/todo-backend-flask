from app import db
from dao.model import *
from datetime import datetime


def create_todolist(data):
    """
    Create new todolist
    :return:
    """
    todolist = TodoList(title=data.title,
                        lastModfied=datetime.utcnow(),
                        items=data.items
                        )
    db.session.add(todolist)
    db.session.commit()


def get_todolists():
    """
    Retrieve all todolists
    :return:
    """
    todolists = TodoList.query.order_by(TodoList.id).all()
    return todolists


def get_todolist(todolist_id):
    """
    Retrieve todolist by id
    :param todolist_id:
    :return:
    """
    todolist = TodoList.query.filter_by(todolist_id=todolist_id).first()
    return todolist


def update_todolist(todolist_id, data):
    """
    Update todolist by id, record current timestamp, update modifieddate
    :param todilist_id:
    :param todolist:
    :return:
    """
    todolist = TodoList.query.filter_by(todolist_id=todolist_id).first()
    currentTimeStamp = datetime.utcnow()
    modifiedTime = ModifiedDate(currentTimeStamp)
    todolist.title = data.title
    todolist.lastModified = currentTimeStamp
    todolist.items = data.items
    db.session.add(modifiedTime)
    db.session.commit()


def delete_todolist(todolist_id):
    """
    Delete todolist by id
    :param todolist_id:
    :return:
    """
    modifiedDates = ModifiedDate.filter_by(todolistId=todolist_id)
    todolist = TodoList.query.filter_by(todolist_id=todolist_id).first()
    db.session.delele(modifiedDates)
    db.session.delete(todolist)
    db.session.commit()
