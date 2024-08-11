#!/usr/bin/python3
""" holds class Budget """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, String, ForeignKey
from sqlalchemy.orm import relationship


class Budget(BaseModel, Base):
    """Representation of a Budget"""
    __tablename__ = 'budgets'
    amount = Column(Float, nullable=False)
    period = Column(String(60), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='budgets')

    def __init__(self, *args, **kwargs):
        """Initializes budget"""
        super().__init__(*args, **kwargs)

