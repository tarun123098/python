#set dict 
#unordered #ordered (after py 3.7 version before unordered)
#not indexed(not everytime) #indexed 
# mutable(we cant change or replace eleemnts but we can add/remove) #mutable
# no duplicates #key shouldn't be duplicate
a={1,2,3,4,5,5,"Tarun"}
print(type(a))
a.add("true")
print(a)
#dictonarires  property(key)     data(value) dict is commbo of key and value0
#                  name              TArun
 #                  age             20
#              marks1                55 
 #               marks2               65
b = {'name': 'Tarun', 'age': 10, 'marks': 55, 'm2': 55}
print(type(b))
print(b.get('age')) #output 10
print(b.keys())
for i in b:#i: Represents each key in the dictionary during each iteration of the loop.
    print(b.get(i))
    print(i)#prints key names
#b.update({'age':11})