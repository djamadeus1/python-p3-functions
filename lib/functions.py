#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(Naureen):
    print(f"Hello, {Naureen}!")

def greet_with_default(Sunny="programmer"):
    print(f"Hello, {Sunny}!")

def add(Num45, Num55):
    return Num45 + Num55

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2

#def my_function(param):3
   # print("Running myFunction")
    #return param + 1