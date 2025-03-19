from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from typing import TypedDict
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import Union

from .lib.Hash import HashFactory
from .lib.DataBase import UserData,UserDB

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

class ErrorResponse(TypedDict):
    detail: str
    code: int
    
@app.get("/hello-world")
async def hello_world():
    return {"message":"hello"}
    
class LoginRequest(TypedDict):
    account:str
    password:str

@app.post("/login")
async def login(loginrequest:LoginRequest):
    pass
    return {"message":"login"}

class RegisterRequest(TypedDict):
    user_name:str
    password:str
    mail:str

@app.post("/register", response_model=Union[dict, ErrorResponse], responses={400: {"model": ErrorResponse,
                                                                                   "description":"User_name exist error"}})
def register(register_request:RegisterRequest, request: Request):
    client_ip = request.client.host 
    if UserDB.query_user(register_request['user_name']):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User {register_request['user_name']} already exists."
        )
    hash_password = HashFactory.get_hash_method("bcrypt").hash_password(register_request['password'])
    new_user = UserData(
        user_name = register_request['user_name'],
        password = hash_password,
        mail = register_request['mail'],
        created_at = datetime.now(),
        last_login_ip = client_ip
    )
    UserDB.register_user(new_user)
    return {"message": "User successfully registered", "user_name": register_request['user_name']}