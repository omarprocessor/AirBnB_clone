#!/usr/bin/python3
"""
Moduli: file_storage.py

Inafafanua darasa la `FileStorage`.
"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage():
    """
    inafanya serializes ya instances katika faili la JSON na
    deserializes faili la JSON kuwa instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        inarudisha dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        inafuta katika __objects obj na ufunguo <jina la darasa la obj>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        inafanya serializes __objects katika faili la JSON (njia: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {key: value.to_dict() for key, value in FileStorage.__objects.items()}, f)

    def reload(self):
        """
        inafanya deserializes faili la JSON kuwa __objects tu ikiwa faili la JSON
        linapatikana; vinginevyo, halifanyi chochote
        """
        current_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return

            FileStorage.__objects = {
                key: current_classes[key.split('.')[0]](**value)
                for key, value in deserialized.items()}
