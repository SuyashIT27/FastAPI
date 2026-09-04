from fastapi import FastAPI
app=FastAPI()
#Creating the post request
@app.post("/form")
def formFilling(name:str=None,age:int=0):
  return{
    "Name":name,
    "Age":age
  }
#best way is to use Dictionary 
@app.post("/data")
def data(userData:dict):
  return{
    "message":"Message sent sucessfully",
    "data":userData
  }
#using the pydantic to validate the data 
from pydantic import BaseModel
class username(BaseModel):
  name:str
  age:int
@app.post("/username")
def username(username:username):
  return{
    "Message":"Get the username sucessfully",
    "data":username  
    }  
