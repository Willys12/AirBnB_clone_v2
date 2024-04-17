#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ Rep. MySQL database
    Attr:
        _tablename__ (str): The name of MySQL table to store

    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def cities(self):
            """Returns the list of `City` instances
            with `state_id` equals to the current
            """

            city_nms = []

            for _id, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    cities.append(city)

            return city_nms
