#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
import os


class State(BaseModel, Base):
    """ State class """

    if os.environ["HBNB_TYPE_STORAGE"] == "db":
        cities = relationship("City", cascade="all, delete")
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
    else:
        name = ""
