#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
     """Represents a database storage engine.

    Attr:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """
    __engine = None
    __session = None

    def __init__ (self):
        """Initializing DBStorage"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        
        self.__engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@{host}/{db}", pool_pre_ping=True)
        
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

        self.reload()
    
    def all(self, cls=None):
         """Query on the curret database session all objects of the given class.

        If cls is None, queries all types of objects.

        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
         if cls is None:
            classes_to_query = [User, State, City, Amenity, Place, Review]
        else:
            classes_to_query = [cls]

        objs = []
        for cls in classes_to_query:
            objs.extend(self.__session.query(cls).all())

        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}
     
    def new(self, obj):
        """Adding obj to the current db session."""
        self.__session.add(obj)

    def save(self):
        """Commiting all changes to the current db session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deleteing obj from the current db session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the db and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        call remove() method on the private session attribute (self.__session)
        tips or close() on the class Session tips
        """
        self.__session.remove()
