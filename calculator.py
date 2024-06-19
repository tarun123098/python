a=int(input("enter a number:"))
b=int(input("enter b number:"))
c=input("what operation you want to do: ")
if (c == "+" or c == "addition"):
    print(f"Addition of {a} and {b} is {a+b}" )
elif(c == "-" or c == "subtraction"):
    print(f"subtraction of {a} and {b} is {a-b}")
elif(c == "*" or c == "multiplication"):
    print(f"multiplication of {a} and {b} is {a*b}")
elif(c == "/" or c == "division"):
    print(f"division of {a} and {b} is {a/b}")
elif(c == "//" or c == "floatdivison"):
    print(f"float d of {a} and {b} is {a//b}")
elif(c == "%" or c == "remainder"):
    print(f"remainder  of {a} and {b} is {a%b}")
elif(c == "**" or c == "power"):
    print(f"power of {a} and {b} is {a**b}")
else:
    print("enter correct operator")
    