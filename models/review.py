#!/usr/bin/python3
# Alex-reid44 and Joyclare

"""New class inherit from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review that inherit from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
