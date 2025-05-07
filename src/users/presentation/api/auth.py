from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Body

from src.users.domain.use_cases.login.entities import LoginRequest
from src.users.domain.use_cases.login.interfaces import ILoginUseCase
from src.users.domain.use_cases.refresh.interfaces import IRefreshUseCase
from src.users.domain.use_cases.register.entities import RegisterRequest
from src.users.domain.use_cases.register.interfaces import IRegisterUseCase
from src.users.presentation.schemas.auth import TokenResponse, UserBody, RegisterResponse
from src.users.presentation.schemas.exceptions import UnauthorizedSchema, UserDataConflictSchema

router = APIRouter()


@router.post("/login", response_model=TokenResponse,
             responses={401: {"model": UnauthorizedSchema}}
             )
@inject
async def login(form: UserBody, login_use_case: FromDishka[ILoginUseCase]):
    return await login_use_case.execute(
        LoginRequest(
            email=form.email,
            password=form.password
        )
    )


@router.post("/register", response_model=RegisterResponse, responses={
    409: {"model": UserDataConflictSchema},
})
@inject
async def register(form: UserBody, register_use_case: FromDishka[IRegisterUseCase]):
    return await register_use_case.execute(
        RegisterRequest(
            email=str(form.email),
            password=form.password
        )
    )


@router.post("/refresh", response_model=TokenResponse)
@inject
async def refresh(refresh_use_case: FromDishka[IRefreshUseCase], refresh_token: str = Body(..., embed=True)):
    return await refresh_use_case.execute(refresh_token)
