import bcrypt


class PasswordBcrypt:
    def verify_password(self, password: str, hash_password: bytes) -> bool:
        password_bytes = password.encode('utf-8') if isinstance(password, str) else password
        return bcrypt.checkpw(password_bytes, hash_password)

    def hash_password(self, password: str) -> str:
        password_bytes = password.encode('utf-8') if isinstance(password, str) else password
        return str(bcrypt.hashpw(password_bytes, bcrypt.gensalt()))
