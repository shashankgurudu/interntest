from sympy import *
from sympy.abc import *
lines = [line.strip('\n') for line in open('sample.txt')]
line = []
for a in lines:
	line.append(diff(a,x))
	line.append(integrate(a,x))
	line.append(summation(b,(i,1,10)))
	line.append(solve(a,x))
	line.append(series(sin(x),x))
print line

with open('output.txt','a') as out:
	for b in line:
		out.write(str(b))
		out.write('\n')