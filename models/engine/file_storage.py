#!/usr/bin/python3
"""
FileStorage module

This module defines the FileStorage class which handles serialization
and deserialization of instances to/from JSON file.
"""
import json
import os


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

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects if file exists.
        If file doesn't exist, do nothing (no exception raised).
        """
        if not os.path.exists(FileStorage.__file_path):
            return

        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)

            # Import classes dynamically to avoid ImportError
            class_map = {}
            
            try:
                from models.base_model import BaseModel
                class_map['BaseModel'] = BaseModel
            except ImportError:
                pass
            
            try:
                from models.user import User
                class_map['User'] = User
            except ImportError:
                pass
            
            try:
                from models.state import State
                class_map['State'] = State
            except ImportError:
                pass
            
            try:
                from models.city import City
                class_map['City'] = City
            except ImportError:
                pass
            
            try:
                from models.amenity import Amenity
                class_map['Amenity'] = Amenity
            except ImportError:
                pass
            
            try:
                from models.place import Place
                class_map['Place'] = Place
            except ImportError:
                pass
            
            try:
                from models.review import Review
                class_map['Review'] = Review
            except ImportError:
                pass

            for key, value in obj_dict.items():
                class_name = value['__class__']
                if class_name in class_map:
                    FileStorage.__objects[key] = class_map[class_name](**value)
        except Exception:
            pass
