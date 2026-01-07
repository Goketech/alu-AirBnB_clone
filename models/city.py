#!/usr/bin/python3
"""
City module

This module defines the City class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class represents a city in the AirBnB clone.

    Attributes:
        state_id (str): State ID (will be State.id)
        name (str): City name
    """

    state_id = ""
    name = ""
