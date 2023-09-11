#!/usr/bin/env python3
def greet_programmer():
    print("Hello, programmer", end="!\n")

def greet(name="Naureen"):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    if not isinstance(number, (int, float)): 
        return None
    else:
        return number/2
