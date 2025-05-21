import bcrypt


class PasswordBcrypt:
    def verify_password(self, password: bytes, hash_password: bytes) -> bool:
        print(password, hash_password)
        return bcrypt.checkpw(password, hash_password)

    def hash_password(self, password: str) -> bytes:
        return bcrypt.hashpw(password, bcrypt.gensalt())
