#types of attributes
#clss-functions and variables
#two types of attributes-instance(object) attributes(different for evry obejct)
#class attribbutes(same for all obj of a class)
#instance attribute change for every object
#class attribute and obj are not linked class will work fixed
class person:
    city="hyderabad"#class attribuute is same for evry object will work when we use class name
    def __init__(self,name,age):#name and age are instance attribute it will work only we use self
        self.name=name
        self.age=age
    def GetValue(self):#this will rem
        print(f"the colour of the boy is {self.name} and the age is {self.age} he is from {person.city}.")
p1=person("tarun",18)#object
p1.GetValue()#changed in person obejct
p2=person("ravi",10)#object
p2.GetValue()#chaanged in person object
print(p1.name,p1.age)


    