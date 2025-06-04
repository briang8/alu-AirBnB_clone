#!/usr/bin/python3
"""Defines unnittests for models/review.py."""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Unittests for testing the Review class."""

    def test_is_subclass(self):
        """Check that Review is a subclass of BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_place_id(self):
        """Test that Review has attr place_id, and it's an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
        
        # Test place_id assignment
        review.place_id = "review place_id"
        self.assertEqual(review.place_id, "review place_id")

    def test_user_id(self):
        """Test that Review has attr user_id, and it's an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
        
        # Test user_id assignment
        review.user_id = "review user_id"
        self.assertEqual(review.user_id, "review user_id")

    def test_text(self):
        """Test that Review has attr text, and it's an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")
        
        # Test text assignment
        review.text = "review text"
        self.assertEqual(review.text, "review text")




if __name__ == "__main__":
    unittest.main()
