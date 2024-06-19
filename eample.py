class car:
    def __init__(self):#only write self,name,age if it is not intialised
        self.name="swift"
        self.maxspeed=150
    def GetValue(self):
        print(f"car company is {self.name} and speed is {self.maxspeed}")
c=car()
c.GetValue()
print(c.name,c.maxspeed)