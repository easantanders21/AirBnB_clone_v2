""" Class DBStorage """

import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session, sessionmaker
from console import HBNBCommand


class DBStorage:
    """ Class DBStorage check changes """

    __engine = None
    __session = None

    def __init__(self):

        db = 'mysql+mysqldb://{}:{}@{}/{}'.format(os.environ["HBNB_MYSQL_USER"],
                                                  os.environ["HBNB_MYSQL_PWD"],
                                                  os.environ["HBNB_MYSQL_HOST"],
                                                  os.environ["HBNB_MYSQL_DB"])

        self.__engine = create_engine(db, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
            
    def all(self, cls=None):
        dic_cls = {}
        print(self.__session.query(cls).all())

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def reload(self):
        """create all reload data
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(
            session_factory)
