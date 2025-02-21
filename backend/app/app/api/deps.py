from fastapi import Depends, HTTPException, status, Cookie
from fastapi.security import HTTPAuthorizationCredentials
from jose import JWTError, jwt
from uuid import UUID, uuid4
# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, Generator
from pydantic import BaseModel
from app.core.auth import oauth2_scheme, get_bearer_token
from app.core.config import settings
from app.db.session import SessionLocal, async_session_maker
from app.models.user import User
from app.core.execptions.exception import CredentialsException
from sqlalchemy import select

from app.clients.reddit import RedditClient
from app import crud

from fastapi_sessions.session_verifier import SessionVerifier
from uuid import UUID
from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters
from app.schemas import SessionData

class TokenData(BaseModel):
    # username: Optional[str] = None
    userid: Optional[int]


async def get_db() -> Generator:
    """db = SessionLocal()
    db.current_user_id = None
    try:
        yield db
    finally:
        await db.close()
    """
    async with async_session_maker() as db:
        yield db



def get_reddit_client() -> RedditClient:
    return RedditClient()


# async def get_current_user(db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme) ) -> User:
async def get_current_user(db: AsyncSession = Depends(get_db),
                           auth: Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token),
                           ids_user_access_token:  str = Cookie(default=None)
                           ) -> Optional[User]:
    # skipping for simplicity...
    try:
        if auth is None and ids_user_access_token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Bearer token missing or unknown",
            )
        token = ids_user_access_token if ids_user_access_token else auth.credentials
        print(f'token: {token}')
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud": False},
        )
        # username: str = payload.get("sub")
        # token_data = TokenData(username=username)
        userid: int = int(payload.get("sub"))
        token_data = TokenData(userid=userid)

    except JWTError:
        raise CredentialsException

    query = select(User).where(User.id == token_data.userid)
    user = await db.execute(query)
    user = user.scalar_one_or_none()
    if user is None:
        raise CredentialsException(status_code=status.HTTP_401_UNAUTHORIZED,
                                   detail="Could not validate credentials",
                                   headers={"WWW-Authenticate": "Bearer"})
    return user
    # skipping for simplicity...


async def get_token(auth: Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token), ) -> str:
    # Simulate a database query to find a known token
    if auth is None or (token := auth.credentials) not in known_tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer token missing or unknown",
        )
    return token



cookie_params = CookieParameters()

#use UUID
cookie = SessionCookie(
    cookie_name="cookie",
    identifier="general_verifier",
    auto_error=True,
    secret_key="DONOTUSE",
    cookie_params=cookie_params,
)

backend = InMemoryBackend[UUID, SessionData]()

class BasicVerifier(SessionVerifier[UUID, SessionData]):
    def __init__(
            self,
        *,
        identifier: str,
        auto_error: bool,
        backend: InMemoryBackend[UUID, SessionData],
        auth_http_exception: HTTPException ):
    
        self._identifier = identifier
        self._auto_error = auto_error
        self._backend = backend
        self_auth_http_exception = auth_http_exception
    
    @property
    def identifier(self):
        return self._identifier
    
    @property
    def backend(self):
        return self._backend

    @property
    def auto_error(self):
        return self._auto_error

    @property 
    def auth_http_exception(self):
        return self._auth_http_exception

    def verify_session(self, model: SessionData) -> bool:
        '''If the session exists, it is valid'''
        return True 
    
verifier = BasicVerifier(
    identifier="general_identifier",
    auto_error=True,
    backend=backend,
    auth_http_exception = HTTPException(status_code=403, detail='invalid session'),
)
        