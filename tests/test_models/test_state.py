#!/usr/bin/python3
"""
Unit tests for State class
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_inheritance(self):
        """Test that State inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """Test that State has the correct attributes"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_attribute_defaults(self):
        """Test that State attributes have correct default values"""
        state = State()
        self.assertEqual(state.name, "")

    def test_attribute_assignment(self):
        """Test that State attributes can be assigned"""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")


if __name__ == '__main__':
    unittest.main()
