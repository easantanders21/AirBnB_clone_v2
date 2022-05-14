#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    cities = relationship("City", cascade="all, delete")
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
