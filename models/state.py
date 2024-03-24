#!/usr/bin/python3
"""State class definition."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel, Base
from models.city import City
import models
import shlex


class State(BaseModel, Base):
    """"Class definition for State.
    Attributes:
    name (str): The name of the state.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Return the list of City objects linked to the current State."""
        cities_list = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
