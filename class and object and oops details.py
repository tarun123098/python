#oops means object oriented programming it is used for real world problems....
#entity means object
#entitty ---->1.property
            #2.functonality
            #Example:car-----prop:colourr,weight
                             #funt:start,stop
#in oops there  are two important things 1.class:plan to construct a car
#                                        2.object:swift,volvo cars
# oops: 1.inheritance
         #2.encapsulation
        #3.abstraction
        #4.polymorphism
        #5.Data protection
class Car:
    def SetValue(self, colour, machine):#In the Code: SetValue is the method where you set (or give) these details to your car.
        self.colour = colour
        self.machine = machine

    def GetValue(self):#GetValue (Getting Details):
        print("The colour of the car is", self.colour, "and the type of machine is", self.machine)
# Creating a car using the Car plan
P = Car()
colour = input("Enter the colour of the car: ")
machine = input("Enter the type of machine: ")
# Using SetValue to give these details to your car
P.SetValue(colour, machine)
# Using GetValue to ask the car what its details are
P.GetValue()
#setvalue and getvalue are methods
"""Functionality:

SetValue: Used to set or assign values to attributes of an object.
input: Used to get input from the user.
GetValue: Used to retrieve and display the values of an object's attributes.
print: Used to display text or variables to the console.
Context of Use:

SetValue: Defined inside a class to manage object attributes.
input: Used anywhere in the code to get user input.
GetValue: Defined inside a class to access and display object attributes.
print: Used anywhere in the code to output text.
"""