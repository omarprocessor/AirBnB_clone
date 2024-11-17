#!/usr/bin/python3
"""Jaribio la moduli ya darasa la FileStorage."""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import json
import os


class TestFileStorage(unittest.TestCase):
    """Majaribio ya darasa la FileStorage."""

    def setUp(self):
        """Huandaa mazingira ya jaribio."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Husafisha mazingira ya jaribio."""
        self.setUp()

    def test_storage_initialization(self):
        """Hujaribu kuanzisha mfano wa uhifadhi."""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_init_no_args(self):
        """Hujaribu __init__ bila hoja."""
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        self.assertEqual(
            str(e.exception),
            "descriptor '__init__' of 'object' object needs an argument"
        )

    def test_init_with_many_args(self):
        """Hujaribu __init__ na hoja nyingi."""
        self.setUp()
        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        ujumbe = "FileStorage() takes no arguments"
        self.assertEqual(str(e.exception), ujumbe)

    def test_class_attributes(self):
        """Hujaribu sifa za darasa la FileStorage."""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def helper_test_all(self, class_name):
        """Husaidia kujaribu njia ya all() kwa jina la darasa lililotolewa."""
        self.setUp()
        self.assertEqual(storage.all(), {})

        instance = storage.classes()[class_name]()
        storage.new(instance)
        key = "{}.{}".format(type(instance).__name__, instance.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], instance)

    def test_all_BaseModel(self):
        """Hujaribu njia ya all() kwa BaseModel."""
        self.helper_test_all("BaseModel")

    def test_new(self):
        """Hujaribu njia ya new()."""
        self.setUp()
        instance = BaseModel()
        storage.new(instance)
        key = "{}.{}".format(type(instance).__name__, instance.id)
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], instance)

    def test_save(self):
        """Hujaribu njia ya save()."""
        self.setUp()
        instance = BaseModel()
        storage.new(instance)
        key = "{}.{}".format(type(instance).__name__, instance.id)
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        data = {key: instance.to_dict()}
        with open(
            FileStorage._FileStorage__file_path, "r", encoding="utf-8"
        ) as f:
            self.assertEqual(len(f.read()), len(json.dumps(data)))
            f.seek(0)
            self.assertEqual(json.load(f), data)

    def test_reload(self):
        """Hujaribu njia ya reload()."""
        self.setUp()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        instance = BaseModel()
        storage.new(instance)
        key = "{}.{}".format(type(instance).__name__, instance.id)
        storage.save()
        storage.reload()
        self.assertEqual(instance.to_dict(), storage.all()[key].to_dict())


if __name__ == "__main__":
    unittest.main()
