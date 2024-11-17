#!/usr/bin/python3
"""
Moduli: base_model.py
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Darasa la msingi ambalo linafafanua sifa/methodi
    za kawaida kwa madarasa mengine.
    """

    def __init__(self, *args, **kwargs):
        """
        Huanzisha kitu kipya pamoja na sifa zake.
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        """
        Hurejesha uwakilishi wa maandishi wa mfano.
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Husasisha sifa ya umma `updated_at` na tarehe ya sasa.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Hurejesha kamusi yenye funguo/maadili yote
        ya __dict__ ya mfano.
        """
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict
