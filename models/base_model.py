#!/usr/bin/python3
"""
BaseModel module

This module defines the BaseModel class which serves as the base class
for all models in the AirBnB clone project.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class defines all common attributes/methods for other classes.

    Attributes:
        id (str): unique identifier for each instance
        created_at (datetime): timestamp when instance is created
        updated_at (datetime): timestamp when instance is last updated
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        If kwargs is not empty, recreate instance from a dictionary
        representation. Otherwise, create a new instance and register it
        in storage.

        Args:
            *args: unused
            **kwargs: dictionary representation of an instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Return string representation of the BaseModel instance.

        Returns:
            str: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Update updated_at with the current datetime and save to storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return dictionary representation of the instance.

        Returns:
            dict: all keys/values of __dict__ plus __class__,
                  with datetimes converted to ISO 8601 strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
