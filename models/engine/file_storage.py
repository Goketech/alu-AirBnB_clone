#!/usr/bin/python3
"""
FileStorage module

This module defines the FileStorage class which handles serialization
and deserialization of instances to/from a JSON file.
"""
import json
import os


class FileStorage:
    """
    FileStorage class serializes instances to a JSON file and
    deserializes JSON file to instances.

    Private class attributes:
        __file_path (str): path to the JSON file
        __objects (dict): stores all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects.

        Returns:
            dict: dictionary of all stored objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id.

        Args:
            obj: object to add to storage
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file (path: __file_path).
        """
        obj_dict = {key: obj.to_dict()
                    for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects (if the file exists).

        If the JSON file (__file_path) does not exist, do nothing.
        No exception should be raised in that case.
        """
        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)

        # Import model classes only when reloading to avoid circular imports
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_map = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }

        for key, value in obj_dict.items():
            class_name = value.get("__class__")
            cls = class_map.get(class_name)
            if cls is not None:
                FileStorage.__objects[key] = cls(**value)
