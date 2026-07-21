from passlib.context import CryptContext
from jose import jwt
import crud

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated = "auto"
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def verify_access_token(token: str):

    payload = jwt.decode(
        token,
        crud.SECRET_KEY,
        algorithms=[crud.ALGORITHM]

    )

    user_id = payload.get("sub")

    if user_id is None:
        return None
    
    return user_id