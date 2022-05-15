#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review

import models
import os

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":

        amenities = relationship("Amenity", secondary='place_amenity',
                                 viewonly=False, cascade="all, delete",
                                 backref="places")

        reviews = relationship("Review",
                               cascade="all, delete",
                               backref="place")

    else:
        @property
        def reviews(self):
            """returns the list of City instances with state_id"""
            reviews_list = []
            _reviews = models.storage.all(Review)
            for _review in _reviews.values():
                if self.id == _review.place_id:
                    reviews_list.append(_review)
            return reviews_list

        @property
        def amenities(self):
            """returns the list of City instances with state_id"""
            from models.amenity import Amenity
            amenities_list = []
            _amenities = models.storage.all(Amenity)
            for _amenity in _amenities.values():
                if _amenity.id in self.amenity_ids:
                    amenities_list.append(_amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, arg):
            from models.amenity import Amenity
            if arg.__class__ == Amenity:
                self.amenity_ids = arg
