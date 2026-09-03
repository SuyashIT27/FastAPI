from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
  return{"message":"First api is made"}
