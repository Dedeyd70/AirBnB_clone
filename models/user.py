#!/usr/bin/python3
""" Class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        Inherits from BaseModel

        Attributes:
                   email: string - empty string
                   password: string - empty string
                   first_name: string - empty string
                   last_name: string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def _init_(self, *args, **kwargs):
        """user"""
        super()._init_(*args, **kwargs)
