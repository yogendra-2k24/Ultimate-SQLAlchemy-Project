from passlib.context import CryptContext
from jose import jwt
import crud
from models import User
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone


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
        crud.SECRET_KEY,
        algorithm=crud.ALGORITHM

    )

    user_id = payload.get("sub")

    if user_id is None:
        return None
    
    return user_id