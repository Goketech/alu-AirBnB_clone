#!/usr/bin/python3
"""
Review module

This module defines the Review class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class represents a review in the AirBnB clone.

    Attributes:
        place_id (str): Place ID (will be Place.id)
        user_id (str): User ID (will be User.id)
        text (str): Review text
    """

    place_id = ""
    user_id = ""
    text = ""
