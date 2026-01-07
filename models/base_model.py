#!/usr/bin/python3
"""
BaseModel module

This module defines the BaseModel class which serves as the base class
for all models in the AirBnB clone project.
"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines all common attributes/methods for other classes.

    Attributes:
        id (str): Unique identifier for each instance
        created_at (datetime): Timestamp when instance is created
        updated_at (datetime): Timestamp when instance is last updated
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        Args:
            *args: Variable length argument list (not used)
            **kwargs: Arbitrary keyword arguments for recreating instance
                     from dictionary representation
        """

        if kwargs:
            # Recreate instance from dictionary
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    # Convert ISO format string to datetime object
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            # Create new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return string representation of the BaseModel instance.

        Returns:
            str: String in format [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """
        Update the updated_at attribute with current datetime and save
        to storage.
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dictionary representation of the instance.

        Returns:
            dict: Dictionary containing all keys/values of __dict__ plus
                  __class__ key with class name. Datetime objects are
                  converted to ISO format strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            obj_dict[key] = value

        return obj_dict
