#!/usr/bin/python3
"""
FileStorage module

This module defines the FileStorage class which handles serialization
and deserialization of instances to/from JSON file.
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class serializes instances to JSON file and
    deserializes JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file
        __objects (dict): Dictionary storing all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects.

        Returns:
            dict: Dictionary of all objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id.

        Args:
            obj: Object to add to __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file (path: __file_path).
        """
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        try:
            with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
                json.dump(obj_dict, f, indent=2)
        except FileNotFoundError:
            pass

    def reload(self):
        """
        Deserialize the JSON file to __objects if file exists.
        If file doesn't exist, do nothing (no exception raised).
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)

                for key, value in obj_dict.items():
                    self.__objects[key] = eval(
                        f"{value['__class__']}(**{value})")

        except FileNotFoundError:
            pass
