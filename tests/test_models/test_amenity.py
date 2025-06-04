#!/usr/bin/python3
"""Defines unnittests for models/amenity.py."""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing the Amenity class."""

    def test_is_subclass(self):
        """Check that Amenity is a subclass of BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_name(self):
        """Test that Amenity has attr name, and it's an empty string"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
        
        # Test name assignment
        amenity.name = "amenity name"
        self.assertEqual(amenity.name, "amenity name")

if __name__ == "__main__":
    unittest.main()
