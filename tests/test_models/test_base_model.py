#!/usr/bin/python3
"""
Unit tests for BaseModel class
"""
import unittest
import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test cases"""
        pass

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        """Test that BaseModel instance is created correctly"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_unique_id(self):
        """Test that each instance has a unique id"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_str_representation(self):
        """Test string representation of BaseModel"""
        model = BaseModel()
        string = str(model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(model.id, string)

    def test_save_method(self):
        """Test that save method updates updated_at"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method returns correct dictionary"""
        model = BaseModel()
        model.name = "Test Model"
        model.number = 42
        model_dict = model.to_dict()
        
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model_dict['name'], "Test Model")
        self.assertEqual(model_dict['number'], 42)

    def test_create_from_dict(self):
        """Test creating BaseModel from dictionary"""
        model1 = BaseModel()
        model1.name = "Test Model"
        model1.number = 42
        model1_dict = model1.to_dict()
        
        model2 = BaseModel(**model1_dict)
        self.assertEqual(model1.id, model2.id)
        self.assertEqual(model1.created_at, model2.created_at)
        self.assertEqual(model1.updated_at, model2.updated_at)
        self.assertEqual(model1.name, model2.name)
        self.assertEqual(model1.number, model2.number)
        self.assertIsNot(model1, model2)

    def test_datetime_attributes(self):
        """Test that created_at and updated_at are datetime objects"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_dict_iso_format(self):
        """Test that to_dict returns ISO formatted datetime strings"""
        model = BaseModel()
        model_dict = model.to_dict()
        
        created_at = datetime.fromisoformat(model_dict['created_at'])
        updated_at = datetime.fromisoformat(model_dict['updated_at'])
        
        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
