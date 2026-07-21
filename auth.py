from passlib.context import CryptContext
from jose import jwt
import crud
from models import User
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from database import get_db


outh2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKE_EXPIRE_MINUTES = 30


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated = "auto"
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(db: Session, username: str):

    user = (
    db.query(User)
      .filter(User.username == username)
      .first()
    )

    return user


def create_access_token(data: dict):

    # original dictionary data would'nt be change
    to_encode = data.copy()

    # Expiry time
    expire = datetime.now(timezone.utc)+ timedelta(minutes = ACCESS_TOKE_EXPIRE_MINUTES)

    # Added Expiry Time
    to_encode["exp"] = expire

    # Create JWT
    encode_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encode_jwt


def verify_access_token(token: str):

    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]

    )

    user_id = payload.get("sub")

    if user_id is None:
        return None
    
    return user_id

def get_current_user(token: str = Depends(outh2_scheme), db: Session = Depends(get_db)):

    user_id = verify_access_token(token)

    user = db.query(User).filter(User.user_id == user_id).first()

    if user is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
    
    return user