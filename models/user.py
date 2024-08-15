#!/usr/bin/python3
""" holds class User """
from hashlib import md5
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a User"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    expenses = relationship('Expense', back_populates='user')
    incomes = relationship('Income', back_populates='user')
    budgets = relationship('Budget', back_populates='user')

    def __setattr__(self, name, value):
        """ Hash the password """
        if name == "password":
            super(User, self).__setattr__(name,
                                          md5(value.encode()).hexdigest())
        else:
            super(User, self).__setattr__(name, value)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
