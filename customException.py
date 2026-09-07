#we will create the custom error
from fastapi import FastAPI
app=FastAPI()
#creating the class for the custom exception
class userNotFoundException(Exception):
  def __init__(self, name):
    self.name=name
#creating the route to test
@app.get("/user/{name}")
def data(name:str):
  if(name!="Suyash"):
    raise userNotFoundException(name)
  return{
    "name":name
  }