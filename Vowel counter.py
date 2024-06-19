A=input("Enter a word")
A2=A.lower()
a=A2.count("a")
e=A2.count("e")
i=A2.count("i")
o=A2.count("o")
u=A2.count("u")
print(a+e+i+o+u)
#simplified version
word = input("Enter a word: ").lower()
vowel_count = word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')
print(vowel_count)

