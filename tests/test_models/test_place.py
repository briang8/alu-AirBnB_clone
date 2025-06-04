#!/usr/bin/python3
"""Defines unnittests for models/place.py."""
import unittest
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    """Unittests for testing the Place class."""

    def test_is_subclass(self):
        """Check that Place is a subclass of BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_name(self):
        """Test that Place has attr name, and it's an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")
        
        # Test name assignment
        place.name = "place name"
        self.assertEqual(place.name, "place name")

    def test_city_id(self):
        """Test that Place has attr city_id, and it's an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")
        
        # Test city_id assignment
        place.city_id = "place city_id"
        self.assertEqual(place.city_id, "place city_id")
        
    def test_user_id(self):
        """Test that Place has attr user_id, and it's an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")
        
        # Test user_id assignment
        place.user_id = "place user_id"
        self.assertEqual(place.user_id, "place user_id")
        
    def test_description(self):
        """Test that Place has attr description, and it's an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")
        
        # Test description assignment
        place.description = "place description"
        self.assertEqual(place.description, "place description")
        
    def test_number_rooms(self):
        """Test that Place has attr number_rooms, and it's 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, 0)
        
        # Test number_rooms assignment
        place.number_rooms = 5
        self.assertEqual(place.number_rooms, 5)
        
    def test_number_bathrooms(self):
        """Test that Place has attr number_bathrooms, and it's 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, 0)
        
        # Test number_bathrooms assignment
        place.number_bathrooms = 2
        self.assertEqual(place.number_bathrooms, 2)
        
    def test_max_guest(self):
        """Test that Place has attr max_guest, and it's 0"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, 0)
        
        # Test max_guest assignment
        place.max_guest = 10
        self.assertEqual(place.max_guest, 10)
        
    def test_price_by_night(self):
        """Test that Place has attr price_by_night, and it's 0"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, 0)
        
        # Test price_by_night assignment
        place.price_by_night = 100
        self.assertEqual(place.price_by_night, 100)
        
    def test_latitude(self):
        """Test that Place has attr latitude, and it's 0.0"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place.latitude, 0.0)
        
        # Test latitude assignment
        place.latitude = 37.7749
        self.assertEqual(place.latitude, 37.7749)
        
    def test_longitude(self):
        """Test that Place has attr longitude, and it's 0.0"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place.longitude, 0.0)
        
        # Test longitude assignment
        place.longitude = -122.4194
        self.assertEqual(place.longitude, -122.4194)
        
    def test_amenity_ids(self):
        """Test that Place has attr amenity_ids, and it's an empty list"""
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place.amenity_ids, [])
        
        # Test amenity_ids assignment
        place.amenity_ids = ["id1", "id2", "id3"]
        self.assertEqual(place.amenity_ids, ["id1", "id2", "id3"])




if __name__ == "__main__":
    unittest.main()
