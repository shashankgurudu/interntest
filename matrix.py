import numpy as np
def matadd(x,y,m1,n1,m2,n2):
	x = np.array(x).reshape(m1,n1)
	y = np.array(y).reshape(m2,n2)

	print x+y

def matsub(x,y,m1,n1,m2,n2):
	x = np.array(x).reshape(m1,n1)
	y = np.array(y).reshape(m2,n2)
	print x-y

def matmul(x,y,m1,n1,m2,n2):
	x = np.array(x).reshape(m1,n1)
	y = np.array(y).reshape(m2,n2)
	print x*y

def matdiv(x,y,m1,n1,m2,n2):
	x = np.array(x).reshape(m1,n1)
	y = np.array(y).reshape(m2,n2)
	print x/y