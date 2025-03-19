from fastapi import FastAPI, Request
from typing import TypedDict
from fastapi.middleware.cors import CORSMiddleware

from .lib.Hash import HashFactory
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

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
    account:str
    password:str
    mail:str

@app.post("/register")
def register(register_request:RegisterRequest, request: Request):
    client_ip = request.client.host 
    hash_password = HashFactory.get_hash_method("bcrypt").hash_password(register_request['password'])
    