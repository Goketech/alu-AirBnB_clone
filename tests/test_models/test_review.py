#!/usr/bin/python3
"""
Unit tests for Review class
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_inheritance(self):
        """Test that Review inherits from BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """Test that Review has the correct attributes"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_attribute_defaults(self):
        """Test that Review attributes have correct default values"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
