class JwtService:
    def __init__(self, config):
        self._access_key = config.JWT_ACCESS_SECRET_KEY
        self._refresh_key = config.JWT_REFRESH_SECRET_KEY
        self._access_expiration = config.ACCESS_TOKEN_EXPIRE_MINUTES
        self._refresh_expiration = config.REFRESH_TOKEN_EXPIRE_MINUTES
        self._algo = config.ALGORITHM

    def encode(self, payload: Payload, _is_refresh: bool = False) -> Token:
        data = asdict(payload)
        now = datetime.utcnow()
        if _is_refresh:
            data["exp"] = now + timedelta(days=self._refresh_expiration)
            key = self._refresh_key
        else:
            data["exp"] = now + timedelta(minutes=self._access_expiration)
            key = self._access_key

        return jwt.encode(data, key, algorithm=self._algo)

    def decode(self, token: str, _is_refresh: bool = False) -> Payload:
        key = self._refresh_key if _is_refresh else self._access_key
        data = jwt.decode(token, key, algorithms=[self._algo])
        return Payload(**data)
