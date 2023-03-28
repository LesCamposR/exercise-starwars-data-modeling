import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column (String(50), nullable=False)
    pass

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    pass

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    pass

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    People_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People)

    Planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

    Vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    Vehicles = relationship(Vehicles)
    pass

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')