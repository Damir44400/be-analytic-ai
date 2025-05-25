from typing import Protocol


class IPasswordBcrypt(Protocol):
    def verify_password(self, password: str, hash_password: str) -> bool:
        pass

    def hash_password(self, password: str) -> bytes:
        pass
