from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

from ..config import settings
from ..database import get_db


# ── Setup ─────────────────────────────────────────────
router = APIRouter()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login"
)


# ── Response Model ────────────────────────────────────
class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    role: str
    full_name: str
    district: str | None


# ── Helper Functions ──────────────────────────────────
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Plain password + bcrypt hash compare කරනවා
    True = match, False = no match
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_token(data: dict) -> str:
    """
    JWT token create කරනවා
    data = {"sub": email, "role": role, ...}
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.token_expire_minutes
    )
    to_encode["exp"] = expire
    return jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm
    )


# ── Login Endpoint ────────────────────────────────────
@router.post("/login", response_model=TokenResponse)
async def login(
    email: str = Body(...),
    password: str = Body(...),
    db: Session = Depends(get_db)
):
    """
    Login endpoint
    email + password → JWT token return
    """

    # Step 1: DB ෙකෙන් user find කරනවා
    result = db.execute(
        text(
            "SELECT * FROM users "
            "WHERE email = :email "
            "AND is_active = true"
        ),
        {"email": email}
    ).fetchone()

    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # Step 2: Password verify කරනවා
    if not verify_password(password, result.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # Step 3: JWT token create කරනවා
    token = create_token({
        "sub":      result.email,
        "role":     result.role,
        "name":     result.full_name,
        "district": result.district,
    })

    # Step 4: Token return කරනවා
    return TokenResponse(
        access_token=token,
        token_type="bearer",
        role=result.role,
        full_name=result.full_name,
        district=result.district,
    )


# ── Protected Route Dependency ────────────────────────
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """
    Protected endpoints use කරන dependency
    JWT token verify → user data return
    
    Usage:
        @router.get("/data")
        async def data(user = Depends(get_current_user)):
            return {"role": user["role"]}
    """
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Token decode කරනවා
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm]
        )
        email = payload.get("sub")
        if email is None:
            raise credentials_error

    except JWTError:
        raise credentials_error

    # DB ෙකෙන් user verify කරනවා
    result = db.execute(
        text(
            "SELECT * FROM users "
            "WHERE email = :email "
            "AND is_active = true"
        ),
        {"email": email}
    ).fetchone()

    if result is None:
        raise credentials_error

    return {
        "email":    result.email,
        "role":     result.role,
        "name":     result.full_name,
        "district": result.district,
    }