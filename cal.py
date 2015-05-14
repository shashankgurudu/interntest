import math
import operator
a = float(input("enter first number"));
b = float(input("enter second number"));
c = raw_input("what do want to do with them + - * /");
basic(c)

print a,b


def basic(c):
	if c == '+':
		print "sum is ", operator.add(a,b)
	elif c == '-':
		print "difference is ", operator.sub(a,b)
	elif c == '*':
		print "multiplication is ", operator.mul(a,b)
	elif c == '/':
		print "division is ", operator.div(a,b)

def adv():
	d = [a,b]
	print math.pow(a,b)
	print math.sqrt(a)
	print operator.mod(a,b)

