"""Module to define schemas of all the objects"""
from pydantic import BaseModel

class UserBaseModel(BaseModel):
    """Definig Users BaseModel"""
    emailID: str
    role: str
    projectID: str
    password: str
