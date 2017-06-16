import numpy as np

a = np.array([[1,1],[0,1]])
b = np.arange(4).reshape(2,2)

print(a)
print(b)
# c = a - b
# print (c)
# print(np.sin(b))
# print (a[a>10])
c = a * b
c_dot = np.dot(a,b)
c_dot2 = a.dot(b)

print(c)
print(c_dot)
print(c_dot2)
