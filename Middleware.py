# Making first Middleware
from fastapi import FastAPI,Request
app=FastAPI()
@app.middleware("http")
async def my_First_Middleware(request:Request,call_next):
  print("Request Received")
  response=await call_next(request)
  print("response Sent")
  return response

