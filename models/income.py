#!/usr/bin/python3
""" holds class Income """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, String, ForeignKey
from sqlalchemy.orm import relationship


class Income(BaseModel, Base):
    """Representation of an Income"""
    __tablename__ = 'incomes'
    amount = Column(Float, nullable=False)
    source = Column(String(128), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='incomes')

    def __init__(self, *args, **kwargs):
        """Initializes income"""
        super().__init__(*args, **kwargs)
