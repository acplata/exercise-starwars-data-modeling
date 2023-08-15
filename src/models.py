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

    characters = relationship("character", backref="user")
    planets = relationship("Planet", backref="user")
    vehicles = relationship("Vehicle", backref="user")

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(Integer, nullable=False)
    hair_color = Column(String(10), nullable=False)
    eye_color = Column(String(10), nullable=False)
    gender = Column(String(10), nullable=False)
    birth_year = Column(String(10), nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    
    planets = relationship("Planet", backref="post")
    vehicles = relationship("Vehicle", backref="post")

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(100), nullable=False)
    terrain = Column(String(100), nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    character_id = Column(Integer, ForeignKey("character.id"), nullable=True)
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"), nullable=True)

class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    passengers = Column(Integer, nullable=False)
    model = Column(String(100), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    starship_class = Column(String(100), nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("character.id"), nullable=False)

    planets = relationship("Planet", backref="planet")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
