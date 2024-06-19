a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))
d=((b**2)-4*a*c)
"""   root formula 
(-b+ or - root b sqaure-4ac)/2a"""
root1=(-b+(d**0.5))/2*a
root2=(-b-(d**0.5))/2*a
print(f"roots:({root1,root2})")  #formatting
