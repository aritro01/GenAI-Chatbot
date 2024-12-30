"""This module hashes the passwords before storing"""
from passlib.context import CryptContext

# Initialize CryptContext once and reuse it
pwd_context = CryptContext( schemes=["sha256_crypt", "md5_crypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Hashes the password using bcrypt"""
    return pwd_context.hash(password)

def verify_hash(password: str, storedhash: str) -> bool:
    """Validate the password with hash"""
    return pwd_context.verify(password, storedhash)
