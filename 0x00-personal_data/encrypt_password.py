#!/usr/bin/env python3
"""Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password"""
    bytes_pwd = password.encode('utf-8')
    hashed_pwd = bcrypt.hashpw(bytes_pwd, bcrypt.gensalt())
    return hashed_pwd


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validating password"""
    bytes_pwd = password.encode('utf-8')
    return bcrypt.checkpw(bytes_pwd, hashed_password)
