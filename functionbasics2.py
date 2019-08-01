#!/usr/bin/env python3

x = int(input("What is the value of x?: "))

def function1():
    int("Call on code...")
    print("...whenever we need it.")

def function2(x):
    return 2*x

def function3(x, y):
    return x + y

def function4():
    return function2(5) + function3(x, 3)

c = function4()
print(c)
