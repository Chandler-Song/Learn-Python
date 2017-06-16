import copy

import numpy as np

a = np.arange(4)
b = a#浅拷贝
c = a.copy()#深拷贝
d = b
a[0] = 11
print(a,b,c)
print(b is a)
print(c is a)