#types of methods or (functions)
#two methods static methods
#instatnec methods    
#same as attribute 
class car:
    def __init__(self):
        self.name="swift"
        self.maxspeed=150
    @staticmethod#without caring instance it prints 
    def hello():
        print("hello")#the output will be same if we call this in any  object
    def GetValue(self):
        print(f"car company is {self.name} and speed is {self.maxspeed}")
c=car()#this is one object
c.GetValue()
c.hello()#also we can call car.hello()
print(c.name,c.maxspeed)
c2=car()
c2.name="ferrari"#now i changed attributes of c2 object
c2.maxspeed=200
c2.hello()
c2.GetValue()
