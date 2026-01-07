#!/usr/bin/python3
"""
Unit tests for Amenity class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """Test that Amenity has the correct attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))

    def test_attribute_defaults(self):
        """Test that Amenity attributes have correct default values"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
