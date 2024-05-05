import bcrypt


def hash_password(password: str) -> bytes:
    """Hash the provided password."""
    pw = bytes(password, "utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw, salt)


def check_password(password: str, password_in_db: str) -> bool:
    password_bytes = password.encode('utf-8')  # Encode the password string
    password_in_db_bytes = password_in_db.encode('utf-8')  # Encode the hashed password string
    return bcrypt.checkpw(password_bytes, password_in_db_bytes)