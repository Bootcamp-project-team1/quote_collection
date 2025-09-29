from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from ..schemas.user_simple import UserCreate, UserResponse   
from ..core.auth import hash_password 

router = APIRouter(prefix="/auth", tags=["Authentication"])
fake_users_db = {}
user_counter = 1

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_create: UserCreate):
    global user_counter

 
    for user in fake_users_db.values():
        if user["email"] == user_create.email:
            raise HTTPException(status_code=400, detail="Email already registered")
        if user["username"] == user_create.username:
            raise HTTPException(status_code=400, detail="Username already taken")
        
    new_user = {
        "id": user_counter,
        "email": user_create.email,
        "username": user_create.username,
        "hashed_password": hash_password(user_create.password),  
        "created_at": datetime.utcnow(),
    }
    fake_users_db[user_counter] = new_user
    user_counter += 1

    return UserResponse(
        id=new_user["id"],
        email=new_user["email"],
        username=new_user["username"],
        is_active=new_user["is_active"],
        created_at=new_user["created_at"],
    )
