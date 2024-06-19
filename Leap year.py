# a year is divisible by both 100 and 400, then it is considered a leap year.
#if year is divisble by 4 it is leap year
Year=input("Enter a year:")
a=int(Year)
if (a % 4 == 0 and (a % 100 != 0 or a % 100 == 0)):
    print("leap year")
else:
    print("not a leap year")
    
    #another model by swaroop
a=int(input("enter a year:"))
leap= False
if a%100 == 0 and a%400 != 0:
    leap = False
elif a%4 == 0:
    leap = True
else:
    leap=False 
print(leap)