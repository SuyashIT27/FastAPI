from fastapi import FastAPI
from pydantic import BaseModel
users=[]
StudentName=None
app=FastAPI()
class dataFormat(BaseModel):
  name:str
  age:int
#creating the get request
@app.get("/user")
def userData():
  return{
    "Meaasge":"Data fetch sucessfully",
    "Name":users
  }
#posting the data with queryparam
@app.post("/user")
def userData(data:dataFormat,name:str=None):
  users.append(data)
  global StudentName
  StudentName =name
  return{
      "dataposted":"done",
      "data":data,
      "name":name
  }