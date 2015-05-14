import numpy as np

print np.zeros(9)
print np.ones(9)

a = np.zeros(9)
b = a.reshape(3,3)
print b

Z = np.eye(3)
print Z

z = np.arange(1,26).reshape(5,5)
print z