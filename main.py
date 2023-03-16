from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
import redis
import random
app=FastAPI()

class SendOtpSchema(BaseModel):
    username:str
@app.post("/sent-otp")
def send_otp(data:SendOtpSchema):
    r=redis.Redis(host='localhost',port=6379)
    # create random 4 digit code
    otp = random.randint(1000,9999)
    r.set(data.username,otp,ex=120)
    print(data.username)
    return {"username":data.username,"otp":otp}
class VerifyOtpSchema(BaseModel):
    username:str
    otp:int
@app.post("/verify-otp")
def verify_otp(data:VerifyOtpSchema):
    r=redis.Redis(host='localhost',port=6379)
    if r.get(data.username):
        if int(r.get(data.username).decode("UTF-8")) == int(data.otp):
            # set username->"otp-verified"
            r.set(data.username,"otp-verified",ex=120)
            return JSONResponse(content={"detail":"otp verified"},status_code=200)
        else:
            raise HTTPException(detail="otp not verified",status_code=400)
    else:
        raise HTTPException(detail="otp expired",status_code=400)
class LoginSchema(BaseModel):
    username:str
    password:str
@app.post("/login-otp")
def login_user(data:LoginSchema):
    r=redis.Redis(host='localhost',port=6379)
    if r.get(data.username):
        return JSONResponse(content={"detail":"login success"},status_code=200)
        # print("login successfull")
    else:
        raise HTTPException(detail="user's mobile is not verified.Please verrify your mobile no. and then login ",status_code=401)
    # raise HTTPException(detail="",status_code=400)