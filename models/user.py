#!/usr/bin/python3
"""
User module

This module defines the User class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class represents a user in the AirBnB clone.

    Attributes:
        email (str): User's email address
        password (str): User's password
        first_name (str): User's first name
        last_name (str): User's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
