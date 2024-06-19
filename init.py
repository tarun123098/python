class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def GetValue(self):
        print(f"the colour of the boy is {self.name} and the age is {self.age}")
name=input()
age=int(input())
p=person(name,age)
p.GetValue()
#init is constructor
#constructors are two types1.default(only self)
                           #2.paramitarised(self,name,age)
#functions start and end with underscore is called dunder methods
