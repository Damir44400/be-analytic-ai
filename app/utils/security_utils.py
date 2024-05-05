import bcrypt


def hash_password(password: str) -> bytes:
    """Hash the provided password."""
    pw = bytes(password, "utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw, salt)


import bcrypt


def check_password(password: str, password_in_db: str) -> bool:
    password_bytes = password.encode('utf-8')

    if isinstance(password_in_db, bytes):
        password_in_db = password_in_db.decode('utf-8')

    return bcrypt.checkpw(password_bytes, password_in_db.encode('utf-8'))
