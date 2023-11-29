from fastapi import HTTPException,status


def raise_not_found_exception(detail: str):
    raise HTTPException(
        detail=detail,
        status_code=status.HTTP_404_NOT_FOUND
    )