from fastapi import FastAPI
app=FastAPI()
#creating the homepage 
@app.get("/")
def home():
  return {"message":"This is homepage"}
#Home route
@app.get("/home")
def Homepage():
  return{"Student":"This is suyash verma"}
#contact route
@app.get("/contact")
def contact():
  return{"Contact":"My mobile number is 9118848131"}
#now creating the dynamic routing
@app.get("/user")
def user():
  return {"User":"This is user"}
@app.get("/user/{number}")
def UserNumber(number):
  return {"user":"hey user with is "+number}
#Now creating the query params 
@app.get("/username")
def userName(name:str=None):
  return {"name":name}

