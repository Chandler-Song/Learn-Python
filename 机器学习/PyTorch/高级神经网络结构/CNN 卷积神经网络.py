#莫烦Python
import torch
import torch.nn as nn
from multiprocessing import freeze_support
from torch.autograd import Variable
import torch.utils.data as Data
import torchvision as tv
import matplotlib.pyplot as plt


def main():
    EPOCH = 1               # train the training data n times, to save time, we just train 1 epoch
    BATCH_SIZE = 50
    LR = 0.001              # learning rate
    DOWNLOAD_MNIST = False

    train_data = tv.datasets.MNIST(
        root = './mnist',
        train = True,
        transform = tv.transforms.ToTensor(),
        download = DOWNLOAD_MNIST
    )



    # Data Loader for easy mini-batch return in training, the image batch shape will be (50, 1, 28, 28)
    train_loader = Data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True,num_workers=2)
    test_data = tv.datasets.MNIST(root='./mnist',train = False)
    test_x = Variable(torch.unsqueeze(test_data.test_data, dim=1), volatile=True).type(torch.FloatTensor)[:2000]/255.   # shape from (2000, 28, 28) to (2000, 1, 28, 28), value in range(0,1)
    test_y = test_data.test_labels[:2000]

    class CNN(nn.Module):
        def __init__(self):
            super(CNN,self).__init__()
            self.conv1 = nn.Sequential(
                nn.Conv2d(
                    in_channels=1,
                    out_channels=16,
                    kernel_size=5,
                    stride = 1,
                    padding=2,
                ),
                nn.ReLU(),
                nn.MaxPool2d(kernel_size=2),
            )
            self.conv2 = nn.Sequential(
                nn.Conv2d(16,32,5,1,2),
                nn.ReLU(),
                nn.MaxPool2d(2)
            )
            self.out = nn.Linear(32 * 7 * 7,10)

        def forward(self,x):
                x = self.conv1(x)
                x = self.conv2(x)
                x = x.view(x.size(0),-1)
                output = self.out(x)
                return output
    cnn = CNN()
    optimizer = torch.optim.Adam(cnn.parameters(), lr=LR)   # optimize all cnn parameters
    loss_func = nn.CrossEntropyLoss()
    for epoch in range(EPOCH):
        for step, (x, y) in enumerate(train_loader):   # gives batch data, normalize x when iterate train_loader
            b_x = Variable(x)   # batch x
            b_y = Variable(y)   # batch y

            output = cnn(b_x)             # cnn output
            loss = loss_func(output, b_y)   # cross entropy loss
            optimizer.zero_grad()           # clear gradients for this training step
            loss.backward()                 # backpropagation, compute gradients
            optimizer.step()

            if step%50 == 0:
                test_output = cnn(test_x)
                pred_y = torch.max(test_output, 1)[1].data.squeeze()
                accuracy = sum(pred_y == test_y) / float(test_y.size(0))
                print('Epoch: ', epoch, '| train loss: %.4f' % loss.data[0], '| test accuracy: %.2f' % accuracy)

    test_output, _ = cnn(test_x[:10])
    pred_y = torch.max(test_output, 1)[1].data.numpy().squeeze()
    print(pred_y, 'prediction number')
    print(test_y[:10].numpy(), 'real number')

if __name__ == '__main__':
    freeze_support()
    main()