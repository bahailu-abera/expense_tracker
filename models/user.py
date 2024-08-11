#!/usr/bin/python3
""" holds class User """
from hashlib import md5
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a User"""
    __tablename__ = 'users'
    username = Column(String(60), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)

    expenses = relationship('Expense', back_populates='user')
    incomes = relationship('Income', back_populates='user')
    budgets = relationship('Budget', back_populates='user')

    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super().__init__(*args, **kwargs)

    def set_password(self, password):
        """Hashes password"""
        self.password_hash = md5(password.encode()).hexdigest()