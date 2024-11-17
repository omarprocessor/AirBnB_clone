#!/usr/bin/python3
"""Moduli ya `amenity`

Inafafanua darasa moja, `Amenity()`,
ambayo inarithi kutoka darasa la `BaseModel()`.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Huduma inayotolewa na mahali/nyumba.

    Sifa:
        name
    """

    name = ""
