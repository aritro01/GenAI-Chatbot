"""Module to read env variables"""
import os
from dotenv import load_dotenv


class EnvHelper:
    """Reads the environment variables"""
    def __init__(self):
        load_dotenv()
        self.db_name = os.getenv("DB_NAME")
        self.db_username=os.getenv("DB_USERNAME")
        self.db_password=os.getenv("DB_PASSWORD")
        self.db_url=f"postgresql://{self.db_username}:{self.db_password}@{self.db_name}"
