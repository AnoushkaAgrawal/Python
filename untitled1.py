# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 14:33:46 2022

@author: HP
"""

x = 5
x >>= 3
print(x)
x = 0
y = 5

print(x==y)
print(x!=y)
x = 12
print(x>2 and x<8)
print(x>8 or x<0)
print(not(x>16 and x>3))


r = 2
print(2*22/7*r*r)
a = 1
b = 2
print(a==b)

rains = 1 
if rains==1:
    print("umbrella")
#the space before print is indentation
#if it rains i will take an umbrella else i wont take it
rain = 1
if rain==1:
    print("y")
else:
    print("r")

rain = 2
snow = 2
if rain==2 and snow==2:
    print("jacket")
#if it rains i take umbrella else if it snow i take jacket
if rain==2:
    print("h")
elif snow==2:
    print("o")
if rain==2 and snow==2:
    print("d")
#datastructure
#lists
k1 = [1,2,3,4]
print(k1)
print(k1)
      
l1 = [1,8,9]
l1.append(0)
print(l1)


     
        
    