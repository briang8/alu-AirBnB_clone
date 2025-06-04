#!/usr/bin/python3
"""Defines unnittests for models/user.py."""
import os
import pep8
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Unittests for testing the User class."""

    @classmethod
    def setUpClass(cls):
        """User testing setup.
        Temporarily renames any existing file.json.
        Resets FileStorage objects dictionary.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.filestorage = FileStorage()
        cls.user = User(email="poppy@holberton.com", password="betty98")


    @classmethod
    def tearDownClass(cls):
        """User testing teardown.
        Restore original file.json.
        Delete the FileStorage, DBStorage and User test instances.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.user
        del cls.filestorage

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(User.__doc__)

    def test_attributes(self):
        """Check for attributes."""
        us = User(email="a", password="a")
        self.assertEqual(str, type(us.id))
        self.assertEqual(datetime, type(us.created_at))
        self.assertEqual(datetime, type(us.updated_at))
        self.assertTrue(hasattr(us, "email"))
        self.assertTrue(hasattr(us, "password"))
        self.assertTrue(hasattr(us, "first_name"))
        self.assertTrue(hasattr(us, "last_name"))

    def test_is_subclass(self):
        """Check that User is a subclass of BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_init(self):
        """Test initialization."""
        self.assertIsInstance(self.user, User)


    def test_init_args_kwargs(self):
        """Test initialization with args and kwargs."""
        dt = datetime.utcnow()
        st = User("1", id="5", created_at=dt.isoformat())
        self.assertEqual(st.id, "5")
        self.assertEqual(st.created_at, dt)
    
    def test_email(self):
        """Test that User has attr email, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")
        
        # Test email assignment
        user.email = "test@example.com"
        self.assertEqual(user.email, "test@example.com")

    def test_password(self):
        """Test that User has attr password, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")
        
        # Test password assignment
        user.password = "12345"
        self.assertEqual(user.password, "12345")

    def test_first_name(self):
        """Test that User has attr first_name, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
        
        # Test first_name assignment
        user.first_name = "Mohamed"
        self.assertEqual(user.first_name, "Mohamed")

    def test_last_name(self):
        """Test that User has attr last_name, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")
        
        # Test last_name assignment
        user.last_name = "Dahab"
        self.assertEqual(user.last_name, "Dahab")




if __name__ == "__main__":
    unittest.main()
