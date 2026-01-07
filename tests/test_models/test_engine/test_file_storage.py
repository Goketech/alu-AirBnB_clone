#!/usr/bin/python3
"""
Unit tests for FileStorage class
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test cases"""
        pass

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_method(self):
        """Test that all() returns the __objects dictionary"""
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new_method(self):
        """Test that new() adds an object to __objects"""
        model = BaseModel()
        key = "BaseModel.{}".format(model.id)
        all_objs = storage.all()
        self.assertIn(key, all_objs)

    def test_save_method(self):
        """Test that save() creates a JSON file"""
        model = BaseModel()
        model.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_method(self):
        """Test that reload() loads objects from JSON file"""
        model = BaseModel()
        model.save()
        
        # Clear storage and reload
        storage._FileStorage__objects = {}
        storage.reload()
        
        key = "BaseModel.{}".format(model.id)
        all_objs = storage.all()
        self.assertIn(key, all_objs)

    def test_save_and_reload(self):
        """Test complete save and reload cycle"""
        model1 = BaseModel()
        model1.name = "Test Model"
        model1.save()
        
        model_id = model1.id
        
        # Reload storage
        storage._FileStorage__objects = {}
        storage.reload()
        
        key = "BaseModel.{}".format(model_id)
        all_objs = storage.all()
        
        self.assertIn(key, all_objs)
        reloaded_model = all_objs[key]
        self.assertEqual(reloaded_model.name, "Test Model")


if __name__ == '__main__':
    unittest.main()
