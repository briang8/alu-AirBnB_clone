#!/usr/bin/python3
import os
import json
import unittest
import models
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage

class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self):
        bm = BaseModel()
        us = User()
        storage.new(bm)
        storage.new(us)
        self.assertIn("BaseModel." + bm.id, storage.all().keys())
        self.assertIn(bm, storage.all().values())
        self.assertIn("User." + us.id, storage.all().keys())
        self.assertIn(us, storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    def test_save(self):
        bm = BaseModel()
        us = User()
        storage.new(bm)
        storage.new(us)
        storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        storage.new(bm)
        storage.new(us)
        storage.save()
        storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == "__main__":
    unittest.main()
