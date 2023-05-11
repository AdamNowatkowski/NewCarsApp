from fastapi import APIRouter, Depends, HTTPException, status, Body, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models import UserBase, LoginBase, CurrentUser
from authentication import AuthHandler

router = APIRouter()
auth_handler = AuthHandler()

@router.post("/register", response_description="Register a new user")
async def register(request: Request, newUser: UserBase = Body(...)) -> UserBase:
    newUser.password = auth_handler.hash_password(newUser.password)
    newUser = jsonable_encoder(newUser)
    
    if (
        existing_mail := await request.app.mongodb["users"].find_one({"email": newUser['email']}) is not None):
        raise HTTPException(status_code=409, detail=f"User with {newUser['email']} already exists")
    
    if ( existing_username := await request.app.mongodb["users"].find_one({"username": newUser["username"]}) is not None):
        raise HTTPException(status_code=409, detail=f"User with {newUser['username']} already exists")
        
    
    user = await request.app.mongodb["users"].insert_one(newUser)
    created_user = await request.app.mongodb["users"].find_one({"_id": user.inserted_id})
    
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)