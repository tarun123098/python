a,b,c=map(int,input("enter your marks in math,scienee,english:").split(","))
Total_marks=a+b+c
print(f"Total marks={Total_marks}")
print(f"Average marks:{(a+b+c)/3}")  #.1f
if(Total_marks >= 252):
    print("Grade:A")
else:
    print("Grade:c")