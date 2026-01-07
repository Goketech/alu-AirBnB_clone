#!/usr/bin/python3
"""
Unit tests for City class
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_inheritance(self):
        """Test that City inherits from BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """Test that City has the correct attributes"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_attribute_defaults(self):
        """Test that City attributes have correct default values"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
