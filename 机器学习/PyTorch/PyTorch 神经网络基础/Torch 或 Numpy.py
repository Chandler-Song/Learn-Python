#莫烦Python
import torch
import numpy as np

np_data = np.arange(6).reshape([2,3])
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()


print(
    '\nnumpy',np_data,
    '\ntorch',torch_data,
    '\ntensor2numpy',tensor2array
)

#abs
data = [-1,-2,1,2]
tensor = torch.FloatTensor(data)    #32bit
print(
    '\nabs',
    '\nnumpy',np.abs(data),
    '\ntensor2numpy',torch.abs(tensor)
)
print(
    '\nabs',
    '\nnumpy',np.sin(data),
    '\ntensor2numpy',torch.mean(tensor)
)

#2 dim
data2 = [[1,2],[3,4]]
tensor1 = torch.FloatTensor(data2)  #32bit
data1 = np.array(data2)
print(
    '\nnumpy',np.matmul(data1,data1),
    '\nnumpy2',data1.dot(data1),
    '\ntensor',torch.dot(tensor1,tensor1)#1*1+....+4*4
)