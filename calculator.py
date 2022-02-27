# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 12:36:52 2022

@author: HP
"""

print("basic calculator")
print("select an opration to perform")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
choice = input("enter your choice :")
num_1 = float(input("enter number 1 : "))
num_2 = float(input("enter number 2 : "))

if choice == "1":
    print(num_1, "+", num_2, "=", (num_1+num_2))
elif choice =="2":
    print(num_1, "-", num_2, "=", (num_1-num_2))
elif choice == "3":
    print(num_1, "*", num_2, "=", (num_1*num_2))
elif choice == "4":
    print(num_1, "/", num_2, "=", (num_1/num_2))
