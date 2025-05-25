import bcrypt


class PasswordBcrypt:
    def verify_password(self, password: str, hash_password: bytes) -> bool:
        return bcrypt.checkpw(password, hash_password)

    def hash_password(self, password: str) -> bytes:
        return bcrypt.hashpw(password, bcrypt.gensalt())
