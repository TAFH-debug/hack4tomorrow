from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated

from sqlalchemy import select, insert
from models import *
from database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

security = HTTPBasic()

async def get_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]) -> User:
    query = select(
        User
    ).where(User.username == credentials.username).where(User.password == credentials.password)
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )
    
    user = await get_db().fetch_one(query)
    
    if not user:
        print(credentials.username)
        print(credentials.password)
        raise unauthed_exc
    
    return user

async def get_project(project: ProjectId, user: User = Depends(get_user)):
    query = select(
        Project
    ).where(Project.id == project.id)
        
    obj: Project = await get_db().fetch_one(query)
    
    if (obj == None) or (obj.user_id != user.id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found!")
    
    return (obj, user)
    
    
@router.get("/basic-auth/")
async def basic_auth(response: Response, user: User = Depends(get_user)):
    response.set_cookie(key="username", value=user.username)
    response.set_cookie(key="password", value=user.password)
    return {"message": "Come to the dark side, we have cookies"}

@router.post("/check-auth/")
async def check_auth(user: UserCreate):
    query = select(
        User
    ).where(User.username == user.username).where(User.password == user.password)
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )
    
    user = await get_db().fetch_one(query)
    
    if not user:
        raise unauthed_exc
        
    return {"result": "ok"}

@router.post("/register/")
async def basic_register(user: UserCreate):
    query = select(
        User
    ).where(User.username == user.username)
    conflict_exc = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Username exists",
    )
    
    iuser = await get_db().fetch_one(query)
    
    if iuser:
        raise conflict_exc
    
    query = insert(
        User
    ).values(username=user.username, password=user.password)
    
    await get_db().execute(query)
    
    return user.username
