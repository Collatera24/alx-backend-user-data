#!/usr/bin/env python3
"""
Module defining the SQLAlchemy User model for the users table.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    User class that maps to the 'users' table in the database.

    Attributes:
        id (int): The primary key of the users table.
        email (str): The user's email, it must be non-nullable.
        hashed_password (str): Hashed password of the usere, also non-nullable.
        session_id (str): A nullable string that stores the session ID.
        reset_token (str): A nullable string that stores the reset token.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
