from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
todos=[]
class ToDo(BaseModel):
  id:int
  title:str
  status:bool
# Sending the todo data
@app.post("/todo")
def create_todo(data:ToDo):
  todos.append(data)
  return{
    "Message":"Task Added sucessfully",
    "Data":data
  }
# Geeting the todo data
@app.get("/todo")
def data():
  return todos
# Geeting the single api data
@app.get("/todo/{todo_id}")
def geetingData(todo_id:int):
  for todo in todos:
    if todo.id==todo_id:
      return {
        "meaagse":"id found",
        "Data":todo
      }
  return {
    "message":"No data is found"
  }
#updating the existing data 
@app.put("/todo/{todo_id}")
def updateData(todo_id:int,data:ToDo):
  for index,todo in enumerate(todos):
    if todo.id==todo_id:
      todos[index]=data
      return{
        "message":"Data updated sucessfully",
        "Data":data
      }
  return {
    "Error":"there is some error"
  }    
#deleting the data
@app.delete("/todo/{todo_id}")
def deletingData(todo_id:int):
  for idx,todo in enumerate(todos):
    if todo.id==todo_id:
      todo.pop(idx)
      return{
        "Message":"Data deleted sucessfully"
      }
  return {
    "Error":"Data not found"
  }  
