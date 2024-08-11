#!/usr/bin/python3
""" holds class Category """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    """Representation of a Category"""
    __tablename__ = 'categories'
    name = Column(String(60), nullable=False)

    expenses = relationship('Expense', back_populates='category')

    def __init__(self, *args, **kwargs):
        """Initializes category"""
        super().__init__(*args, **kwargs)
