from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from helper import demo_save_user

app = FastAPI()

class User(BaseModel):
    username: str
    age:int

class Message(BaseModel):
    content:str
    user:User

@app.post("/users/", response_model=Message)
def create_user(user:User):
      return{"content":"User created successfully!", "user":user}
    
@app.post("/save/",response_model=str)
def save_user(data:User):
    try:
         result = demo_save_user(data)
         return result["result"]
    except Exception as e:
         raise HTTPException(status_code=500,detail="Error occured while saving record in database")