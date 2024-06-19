def add(a,b):
    return a+b
result=add(5,3)
print(result)
#here a,b matches the position 5,3 it is positional args


def personal_info(name,age):
    print("Name:",name)
    print("age:",age)
personal_info(name="tarun",age=20)
#here using keywords we call them so it is calleed as a keyword arguments


def greet_user(name,greeting="hello"):#here we gave default value 
    return greeting+","+name+","
greeting1=greet_user("bob")# here automatically hi is defined at greeting 
greeting2=greet_user("charlie","hi")# when we give hi it changes greeting at hello
print(greeting1)
print(greeting2) 
#default argument means incase no value is passed during function call if no arg is 
#provided then default value will be used this is deafult arguments
   
    
