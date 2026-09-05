#respeonse model is the way to send the data only which we want to send to the user 
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
#Here we will define what data we need to get from the user 
class dataCollection(BaseModel):
  name:str
  age:int
  password:str
#now to make the response model we will make the new class and here we will tell which data we will send 
class dataSending(BaseModel):
  name:str
  age:int
#response_model is used to describe what we will take 
@app.get("/",response_model=dataSending)
def data():
  return{
    "name":"Suyash Verma",
    "age":22,
    "password":"hii"
  }