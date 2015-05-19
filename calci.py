#import calc as c
from numpy import array
import matrix as m
from adv import *
from basic import *
from files import *
from sym import *
a = float(input("enter first number"));
b = float(input("enter second number"));
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)
pow(a,b)
sqrt(a,b)
mod(a,b)


m1 = input("enter m and n of first array")
n1 = input()
m2 = input("enter m and n of second array")
n2 = input()
x = []
y = []
print "enter elements of first array"
for i in range(0,int(m1)*int(n1)):
	x.append(int(input()))
print array(x).reshape(m1,n1)
for i in range(0,int(m2)*int(n2)):
	y.append(int(input()))
print array(y).reshape(m2,n2)

m.matmul(x,y,m1,n1,m2,n2)
m.matadd(x,y,m1,n1,m2,n2)
m.matsub(x,y,m1,n1,m2,n2)
m.matdiv(x,y,m1,n1,m2,n2)

equa()
readwrite()