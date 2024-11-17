#!/usr/bin/python3
"""Moduli ya `state`

Inafafanua darasa moja, `State()`,
ambayo inarithi kutoka darasa la `BaseModel()`.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Jimbo katika programu.

    Sifa:
        name
    """
    name = ""
