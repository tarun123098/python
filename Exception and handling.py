l=[1,2,3,4]
print("index")
i=int(input())
try:
    print(l[i])#by using try the compiler take this as a try and give the error in exception code
except Exception as e:
    print(e)# here it get the error #we can also change thus
print("bye")
#zero divison error
z=int(input())
try:
    a=5/z
except ZeroDivisionError as e:#zero cannt acept as denominator5
    print(e)
finally:
    print("iam inside finally")#exception yes or no dont ccare it will print
print("bye")
#errors are two types:compile time errors #syntax errors easy to resolve and indentify 
# we know before we run the code
                      #run time errors#except syntax errors
#hadnling runtime error is called exception so it is called as a exception handling
#the main use of this exception is the code wont stop running  because of errors