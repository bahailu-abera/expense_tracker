#!/usr/bin/python3
""" holds class Expense """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, String, ForeignKey
from sqlalchemy.orm import relationship

class Expense(BaseModel, Base):
    """Representation of an Expense"""
    __tablename__ = 'expenses'
    amount = Column(Float, nullable=False)
    description = Column(String(128), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    category_id = Column(String(60), ForeignKey('categories.id'), nullable=True)

    user = relationship('User', back_populates='expenses')
    category = relationship('Category', back_populates='expenses')

    def __init__(self, *args, **kwargs):
        """Initializes expense"""
        super().__init__(*args, **kwargs)