from fastapi import APIRouter, status, Request, HTTPException
from pydantic import BaseModel, EmailStr
import bcrypt

from db import prisma
from auth import create_access_token

router = APIRouter()

class MemberSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

@router.post("/sign-up", status_code=status.HTTP_201_CREATED)
async def sign_up(payload: MemberSchema):
    print(payload)

    existing = await prisma.member.find_unique(where={'email': payload.email})

    if existing:
        raise HTTPException(status_code=400, detail='Email already in use')

    async with prisma.tx() as tx:
        member = await tx.member.create(
            data={
                'name': payload.name, 'email': payload.email
            }
        )
        user_pass = payload.password
        bytes = user_pass.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes, salt).decode('utf-8')

        member_password = await tx.member_password.create(data={
            "member_id": member.id,
            "password": hash
        })

    return member

@router.post("/login", status_code=status.HTTP_201_CREATED)
async def login(payload: LoginSchema):
    member = await prisma.member.find_unique(where={'email': payload.email}, include={
        'member_password': True
    })

    print("MEMBER IS")
    print(member)

    if not member:
        raise HTTPException(status_code=400, detail='Invalid email and or password')

    hashed_password = member.member_password.password.encode('utf-8')
    user_password = payload.password.encode('utf-8')

    if not bcrypt.checkpw(user_password, hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid email or password')

    encode = {'id': member.id, 'random': 'cool cat'}
    token = create_access_token(encode)
    
    return {'message': 'Login successful', 'member': member, 'token': token}