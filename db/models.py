"""Table Definitions"""
from sqlalchemy import(Column,
                       String)

from db.database import Base

class Users(Base):
    """Table - GenAIUsers Definition"""
    __tablename__ = "GenAIUsers"
    emailID = Column(String, primary_key=True, index=True)
    role = Column(String, index=True)
    projectID = Column(String, index=True)
    password = Column(String, index=True)
