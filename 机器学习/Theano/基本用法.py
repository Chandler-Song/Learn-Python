#莫烦Python
import numpy as np
import theano.tensor as T
from theano import function

#basic
x = T.dscalar('x')
y = T.dscalar('y')
z = x+y
f = function([x,y],z)

print(f(2,3))

#to pretty-print the function
from theano import  pp
print(pp(z))


#how about matrix
x = T.dmatrix('x') #float 64
y = T.dmatrix('y')
z =T.dot(x,y)
f = function([x,y],z)
print(f(np.arange(12).reshape((3,4)),10*np.ones((3,4))))