from math import *

a = float(input())
b = float(input())
c = float(input())
d = b**2-4*a*c
if d > 0:
    x1 = (-b+sqrt(d))/(2*a)
    x2 = (-b-sqrt(d))/(2*a)
    y1 = max(x1, x2)
    y2 = min(x1, x2)
    print(y2)
    print(y1)
elif d == 0:
    x = -b/(2*a)
    print(x)
else:
    print("Корней нет")
