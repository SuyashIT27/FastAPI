#Dependency injection means making funaction that is dependent on another function or method
#Depends() keyword is use
from fastapi import FastAPI, Depends
app=FastAPI()
def common_logic():
  return{
    "message":"Common Logic Executed"
  }
@app.get("/home")
def home(data=Depends(common_logic)):
  return data