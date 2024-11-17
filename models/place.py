#!/usr/bin/python3
"""Moduli ya `place`

Inafafanua darasa moja, `Place()`,
ambayo inarithi kutoka darasa la `BaseModel()`.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Mahali/nyumba katika programu.

    Inawakilisha mahali/nyumba iliyopakiwa
    na watumiaji wa programu.

    Sifa:
        name
        user_id
        city_id
        description
        number_bathrooms
        price_by_night
        number_rooms
        longitude
        latitude
        max_guest
        amenity_ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
