# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 13:13:16 2022

@author: HP
"""

#lists
mylist = ["yellow","red","blue"]
mylist.append("pink")
print(mylist)
print(len(mylist))
mylist[1:3] = ["purple"]
print(mylist)
mylist.insert(1, "black")
print(mylist)
mylist.remove("pink")
print(mylist)
mylist.sort()
print(mylist)
mylist.copy()
list1 = ["q","k"]
list2 = ["f","d"]
list3 = list1 + list2
print(list3)

#tuples
thistuple = ("sun","moon","sun","star")
print(thistuple)
print(thistuple[2])
print(thistuple[-2])
print(thistuple[1:4])
print(thistuple[3:])
print(thistuple[:3])

thistuple = ("w","o","p")
y = list(thistuple)
y.append("r")
thistuple = tuple(y)
print(thistuple)

#dictionary
mydict = {"v":"k" , "j":"l" , "h":"u"}
print(mydict)
mydict["v"]
mydict.update({"v":"y"})
print(mydict)
mydict["p"] = "l"
print(mydict)
mydict.pop("j")
mydict.copy()

#strings

text = "free things are the best things!"
if "free" in text:

    print("yes")
b = "hello world"
print(b[2:5])    
print(b[5:])
print(b[:7])
print(b[-5:-2])
print(b.upper())
