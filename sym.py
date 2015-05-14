from sympy import *
from sympy.abc import *
a = input("enter the expression")
pprint(a)
print(diff(a,x))
print(integrate(a,x))

b = input("enter expression for summation")

pprint(summation(b,(i,1,10)))
pprint(solve(a,x))
pprint(series(sin(x),x))
expr =a
expr.subs(x,y)
pprint(expr)