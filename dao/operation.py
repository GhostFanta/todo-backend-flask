from dao.model import *
from datetime import datetime


def create_todolist(data):
    """
    Create new todolist
    :return:
    """
    print(data['title'])
    print(data['useremail'])

    todolist = TodoList(title=data['title'],
                        useremail=data['useremail'],
                        lastModfied=datetime.utcnow(),
                        createdDate=datetime.utcnow(),
                        items=data['items']
                        )
    db.session.add(todolist)
    db.session.commit()


def get_todolists(useremail):
    """
    Retrieve all todolists of a user according to useremail
    :return:
    """
    todolists = TodoList.query.filter_by(useremail=useremail).order_by(TodoList.id).all()
    return todolists


def get_todolist(todolist_id):
    """
    Retrieve todolist by id
    :param todolist_id:
    :return:
    """
    todolist = TodoList.query.filter_by(id=todolist_id).first()
    return todolist


def update_todolist(todolist_id, data):
    """
    Update todolist by id, record current timestamp, update modifieddate
    :param todilist_id:
    :param todolist:
    :return:
    """
    todolist = TodoList.query.filter_by(id=todolist_id).first()
    print(todolist)
    currentTimeStamp = datetime.utcnow()
    modifiedTime = ModifiedDate(todolistId=todolist_id, modifiedDate=currentTimeStamp)
    todolist.title = data['title']
    todolist.items = data['items']
    todolist.lastModified = currentTimeStamp
    db.session.add(todolist)
    db.session.add(modifiedTime)
    db.session.commit()


def delete_todolist(todolist_id):
    """
    Delete todolist by id
    :param todolist_id:
    :return:
    """
    modifiedDates = ModifiedDate.query.filter_by(todolistId=todolist_id).all()
    todolist = TodoList.query.filter_by(id=todolist_id).first()
    for dateitem in modifiedDates:
        db.session.delete(dateitem)
    db.session.delete(todolist)
    db.session.commit()
