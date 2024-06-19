#Person--functonaliity--walk,run
#      --properties or data---name,age
#student is subset of person
# a person who is student as some special feautures like rollno,schoolname,bus no(properties)
                                                         # study,read,coding(functonality)
#every stident is person but everypersonn is not a student and that student has some special 
# features as mentioned aabove
#so you have to write two codes one for student and for person and the person code will repeat
#in student to to not the code get repeated  we use inheritance
#person student(we inherit student class from person class)
#a,b,c  a,b,c,d(here person is parent class and  student is child class)
#example
class person:#parent class
    age=20
    def walk(self):
        print("Iam walking")
class student(person):#child class
    rno=15
    def read(self):
        print("Iam reading")
p2=student()
print(p2.rno)

#types of inheritance
#single inheritanec#single parent and single child
#multiple inheritance#father ,mother and child
#multi inheritance#grand parent#parent#child
#hierarichchal inheritance-parent->child1,child2,cdhild3(siblings)
#hybrid inheritance#Multi+multiple inheritance
   