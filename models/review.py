#!/usr/bin/python3
"""Moduli ya `review`.

Inafafanua darasa moja, `Review()`,
ambayo inarithi kutoka darasa la `BaseModel()`.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Mapitio ya mahali/nyumba.

    Inawakilisha mapitio yaliyochapishwa na watumiaji
    wa programu kuhusu mahali/nyumba.

    Sifa:
        text
        user_id
        place_id
    """
    place_id = ""
    user_id = ""
    text = ""
