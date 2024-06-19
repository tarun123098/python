class bike:
    def __init__(self,name,colour):
        self.__name=name#not able to acces outside the class only in the class bcoz it is private
        self.colour=colour
    def GetValue(self):
        print(f"the colour of the good is {self.colour} and  name is {self.__name}")#yes accesbsale
#object
v=bike("bmw","red")
v.GetValue()#method 1 of  accessing data within the class
print(f"the colour of the is {v.__name} and name is {v.colour}")#not able to access outside
#method3 of accesing data outside the class
#now we have a class and object
# #three types of access modifiers public(no resttrictions),private(full restric),protected(partial)
#refer vamsi bhavani video you get clarity\
 #                                     priavte protected public 
  #          --->withiin the sameclass    yes      yes     yes    #accesing
#inheritance---->with in dervied class   no        yes    yes      #accesing
 #          ---->OUTSIDE THE CLASS         no     no      yes     #accesing
  #               example                    __name     _name   name
  # method 1 and 3 are said here method 3 in next file inheritance 
  