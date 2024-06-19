#poly means many
#morphisam meaans rupalu #many foRMs
# a single entity which can able to take multiple forms is called polymorphism\
x=5
y=6
z="Tarun"
w="ravi"
print(x+y)#11 becuase integers it will add
print(z+w)#tarunravi it will  concatination 
#+ is same for both but for int it will add and char it will concanite this is polymorphm example
def mul(a,b,c=1,d=1):#default c=1,d=1
    print(a*b*c*d)
mul(2,3)
mul(2,3,4,5) #c,d has differnt values i alotted so it changed it forms it is SINGLE ENTITY 
#multiple forms it is called polymorphism
class a():
    def test1(self):
        print("it is class a test 1")
class b(a):
    def test1(self):
        print("it is class b test 2")
class c(a):
    def test1(self):
        print("it is class c test 3")
        super().test1()#this will print both parent and child class
class d(c,b):
    def test4(self):
        print("it is class d test 4")
obj=c()
obj.test1()
#here test 1 is same entity but having different forms in the differnent classes (polymorphism)
