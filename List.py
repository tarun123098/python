#list        TUPLE
#orderred     orderred
#indexed      indexed
#mutable     not mutable
#allows duplicate   allows duplicate
l=[1,2,3,2]
T=(1,2,3,2)
print(type(l))
print(type(T))
print(T[0:3])#imp for tuple alsosquare bracket onlly
#starting index included endung index not included
print(l[0])
l[0]=5
print(l)
#T[0]=5 #error because not mutable not able to change
#insert (insert element)
#append (add elemnet end of the list)
l.sort()
l.insert(3,2)
print(l)
 