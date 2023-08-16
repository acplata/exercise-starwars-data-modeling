import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String(60), nullable=False)
    password = Column(String(20), nullable=False)

    favorites = relationship("Favorite", backref="user")

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(Integer, nullable=False)
    hair_color = Column(String(10), nullable=False)
    eye_color = Column(String(10), nullable=False)
    gender = Column(String(10), nullable=False)
    birth_year = Column(String(10), nullable=False)

    favorites = relationship("Favorite", backref="character")
    planet_id = Column(Integer, ForeignKey("planet.id"), nullable=False)
    vehicles = relationship("Vehicle", backref="favorite")

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(100), nullable=False)
    terrain = Column(String(100), nullable=False)

    favorites = relationship("Favorite", backref="planet")
    characters = relationship("Character", backref="planet")

class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    passengers = Column(Integer, nullable=False)
    model = Column(String(100), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    starship_class = Column(String(100), nullable=False)

    favorites = relationship("Favorite", backref="vehicle")
    character_id = Column(Integer, ForeignKey("character.id"), nullable=False)


class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("character.id"), nullable=True)
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"), nullable=True)
    planet_id = Column(Integer, ForeignKey("planet.id"), nullable=True)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
