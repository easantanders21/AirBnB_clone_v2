""" Class DBStorage """

from os import environ
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base

classes = {'BaseModel': BaseModel,
           'User': User,
           'Place': Place,
           'State': State,
           'City': City,
           'Amenity': Amenity,
           'Review': Review}


class DBStorage:
    """ Class DBStorage """

    __engine = None
    __session = None

    def __init__(self):

        db = 'mysql+mysqldb://{}:{}@{}/{}'.format(environ["HBNB_MYSQL_USER"],
                                                  environ["HBNB_MYSQL_PWD"],
                                                  environ["HBNB_MYSQL_HOST"],
                                                  environ["HBNB_MYSQL_DB"])

        self.__engine = create_engine(db, pool_pre_ping=True)

        if environ["HBNB_ENV"] == "test":
            Base.metadata.drop_all(self.__engine)

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
