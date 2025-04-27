class UserBaseException(Exception):
    status_code = 400


class UnauthorizedException(UserBaseException):
    status_code = 401


class UserBadRequestException(UserBaseException):
    pass


class UserAlreadyExistsException(UserBaseException):
    status_code = 409
