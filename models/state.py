#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """

    if os.environ["HBNB_TYPE_STORAGE"] == "db":

        __tablename__ = 'states'

        name = Column(String(128),
                      nullable=False)

        cities = relationship("City",
                              cascade="all, delete",
                              backref="state")


    else:
        name = ""

        @property  # getter
        def cities(self):
            """returns the list of City instances with state_id"""
            cities_list = [] # create type list to return
            _cities = models.storage.all(City) #
            print('------------------------------------------------')
            print(_cities)
            print('------------------------------------------------')
            for _city in _cities.values():
                if self.id == _city.state_id:
                    cities_list.append(_city)
            return cities_list
