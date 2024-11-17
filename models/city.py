#!/usr/bin/python3
"""Moduli ya `city`

Inafafanua darasa moja, `City()`,
ambayo inarithi kutoka darasa la `BaseModel()`.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Jiji katika programu.

    Sifa:
        name
        state_id
    """
    name = ""
    state_id = ""
