#!/usr/bin/python3
"""
Amenity module

This module defines the Amenity class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class represents an amenity in the AirBnB clone.

    Attributes:
        name (str): Amenity name
    """

    name = ""
