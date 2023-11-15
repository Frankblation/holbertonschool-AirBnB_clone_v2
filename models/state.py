#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:

        @property
        def cities(self):
            """list related city objs"""
            new_list = []
            current_list = models.storage.all(City).values()
            for item in current_list:
                item.state_id == self.id:
                new_list.append(item)
            return new_list
