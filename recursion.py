def fact(n):
    factorial = 1
    while n > 0:
        factorial *= n
        n -= 1
    return factorial

# Example usage:
number = int(input("Enter a number: "))
result = fact(number)
print(result)
#this example using looping
#a function that calls itself is called recursion
#to stop the loop we use function inn looping in recursion we called condition as a base condition
#simple by vb
#this example using recurssion
def fact(n): #fact=3
    if n==1 or n==0:#if fact=1 or fact=0 then condition satisfies if not then else
        return 1
    else:
        return n*fact(n-1)#return the 3*fact(2)here recurssion happens then again fact(2)
# now n =2 if condition not satisfies then else 2*fact(1) now n=1 if satisfied return 1 the end
#here function called itself

x=fact(3)
print(x)
"""fact(3) calls fact(2)
fact(2) calls fact(1)
fact(1) returns 1
fact(2) returns 2 * 1 = 2
fact(3) returns 3 * 2 = 6"""

    
    
    