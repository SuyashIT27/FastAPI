# implementing the class 
class car:
  #To create the attribute private use __before the attribute 
  __car_Name=None
  Car_Wheels=None
  Car_Doors=None
  Car_Speed=None
  def __init__(self,name,wheels,doors,speed):
    self.car_Name=name
    self.Car_Wheels=wheels
    self.Car_Doors=doors
    self.Car_Speed=speed
  def get_Name(self):
     return self.car_Name  
#implementing the object
maruti=car("Maruti",4,4,120);
print(maruti.Car_Speed)    
#implementing the inherentance
class ElectricCar(car):
  batteyCapacity=None
  def __init__(self,name,wheels,doors,speed,batteryCapacity):
      super().__init__(name,wheels,doors,speed)
      self.batteyCapacity=batteryCapacity
#creating the class to test super 
tesla=ElectricCar("Tesla",4,4,120,"234Mah")
print("Total Car doors ",tesla.Car_Doors);    
print(tesla.get_Name())

#Testing the polymorphism 
class student:
   name=None
   section=None
   def __init__(self,name):
      self.name=name
   def get_Name(self):
      return self.name   
class Suyash(student):
   name=None
   def __init__(self,name):
      self.name=name
   def get_Name(self):
       return self.name    
test1=student("Shiva")
print(test1.get_Name())
test2=Suyash("Suyash")
print(test2.get_Name())


