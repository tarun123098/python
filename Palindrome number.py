#palindrome means simply radar=radar 121=121 ace=ace two sides same
a=input("enter a word or number:")
if (a == a):
    print("its a palindrome number or word")
else:
    print("not a palindrome number")
#Another method
a="Tarun"
b=a[::-1]#string reversing
if(a==b):
    print("Palindrome number")
else:
    print("not a palindrome number")