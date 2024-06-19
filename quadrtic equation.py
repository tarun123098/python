a,b,c=map(int,input("enter a,b,c:").split(","))
def quadrtic(p,q,r):
    d=((b**2)-4*a*c)
    root1=(-b+(d**0.5))/2*a
    root2=(-b-(d**0.5))/2*a
    print(f"roots:({root1,root2})")  #formatting
result=quadrtic(a,b,c)
print("result")
