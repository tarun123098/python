global_var=10
def number():
    print(global_var)
number()
print(global_var)
#global varaible means which can access anywhere any time becuase it will declare
# ouside of function
def number1():
    global_var1=10
    print(global_var1)
number1()
#print(global_var1)#it wont print because it is local varaible in the function 
