from turtle import *
from math import *
import math

a = float(input("enter the value for a: "))
b = float(input("enter the value for b: "))
c = float(input("enter the value for c: "))

if (a + b >= c) and (b + c >= a) and (c + a >= b):
    print("it's a triangle")

    A = degrees(acos((b**2 + c**2 - a**2)/(2*b*c)))
    B = degrees(acos((c**2 + a**2 - b**2)/(2*c*a)))
    C = degrees(acos((a**2 + b**2 - c**2)/(2*a*b)))
else:
    print("it's not a triangle")