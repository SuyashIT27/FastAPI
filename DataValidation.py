#We will do the data validation with the pydantic 
#This help to Create Schemas , Data Validation , Nested models 
from pydantic import BaseModel
from fastapi import FastAPI
class userData(BaseModel):
  name:str
  age:int
  position:str
app=FastAPI()
@app.post("/userdata")
def userData(data:userData):
  return{
    "Message":"This is the data from the user",
    "Data":data
  }
#To create the nested Data Validation we can inherit that class 
class EmployeeData(BaseModel):
  salery:int
  duration:int
  #This will get the schema from the userData
  userData:userData
@app.post("/employeeData")
def Data(data:EmployeeData):
  return{
    "message":"This is the employee data",
    "Data":data
  }  
