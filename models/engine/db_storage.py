#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.budget import Budget
from models.base_model import Base
from models.category import Category
from models.expense import Expense
from models.income import Income
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Budget": Budget, "Category": Category,
           "Expense": Expense, "Income": Income, "User": User}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        EXPENSE_APP_MYSQL_USER = getenv('EXPENSE_APP_MYSQL_USER')
        EXPENSE_APP_MYSQL_PWD = getenv('EXPENSE_APP_MYSQL_PWD')
        EXPENSE_APP_MYSQL_HOST = getenv('EXPENSE_APP_MYSQL_HOST')
        EXPENSE_APP_MYSQL_DB = getenv('EXPENSE_APP_MYSQL_DB')
        EXPENSE_APP_ENV = getenv('EXPENSE_APP_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(EXPENSE_APP_MYSQL_USER,
                                             EXPENSE_APP_MYSQL_PWD,
                                             EXPENSE_APP_MYSQL_HOST,
                                             EXPENSE_APP_MYSQL_DB))
        if EXPENSE_APP_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(sess_factory)
        self.__session = session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """Retrieve one object"""
        objs = self.all(cls)
        for obj in objs.values():
            if id == obj.id:
                return obj
        return None

    def count(self, cls=None):
        """Counts the number of objects in storage"""
        objs = self.all(cls)
        num_objs = len(objs)
        return num_objs
