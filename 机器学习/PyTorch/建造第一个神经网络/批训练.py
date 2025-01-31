#莫烦Python

import torch
import  torch.utils.data as Data
torch.manual_seed(1)#这是为了重复试验的需要, 固定下伪随机数
BATCH_SIZE = 8

x = torch.linspace(1,10,10)
y = torch.linspace(10,1,10)

torch_dataset = Data.TensorDataset(data_tensor = x,target_tensor = y )
loader = Data.DataLoader(
    dataset=torch_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True,
    num_workers=2,
)

if __name__ == '__main__':
    for epoch in range(3):
        for step,(batch_x,batch_y) in enumerate(loader):
            #training..
            print('Epoch: ', epoch, '| Step: ', step, '| batch x: ',
                  batch_x.numpy(), '| batch y: ', batch_y.numpy())


