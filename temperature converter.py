celsius=int(input("enter number for celsius:"))
farenheit=(celsius*(9/5)+32)
k=273+celsius
print(f"Now celsius number {celsius} is converted into farenheit: {farenheit} and kelvin: {k}")
#another model 
temp=input("enter a number")
a=int(temp)
b=input("enter units(K OR F OR C:)")
if(b == "K"):
    print(f"Temperature in kelvin is:{273+a}K")
elif(b=="F"):
    print(f"Tempearture in kelvin is;{a*(9/5)+32}F")
elif(b=="C"):
    print(f"Temperature in kelvin is:{273+a}K")
    print(f"Tempearture in kelvin is:{a*(9/5)+32}F")
else:
    print("wrong input")


