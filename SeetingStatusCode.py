from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class Structure(BaseModel):
  name:str
  Section:int
#seeting the response code 
@app.get("/", status_code=status.HTTP_404_NOT_FOUND)
def not_found():
    return {"detail": "Item not found"}