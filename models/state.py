#!/usr/bin/python3
"""
State module

This module defines the State class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class represents a state in the AirBnB clone.

    Attributes:
        name (str): State name
    """

    name = ""
