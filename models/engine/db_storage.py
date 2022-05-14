""" Class DBStorage """

import os
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base


class DBStorage:
    """ Class DBStorage """
    __engine = None
    __session = None

    def __init__(self):
        conn = MySQLdb.connect(host=os.environ["HBNB_MYSQL_HOST"],
                               port=3306, user=os.environ["HBNB_MYSQL_USER"],
                               passwd=os.environ["HBNB_MYSQL_PWD"],
                               db=os.environ["HBNB_MYSQL_DB"])

        self.__engine = create_engine(conn, pool_pre_ping=True)