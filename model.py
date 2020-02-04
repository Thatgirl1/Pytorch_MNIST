#Load header file
import torch
import torch.nn as nn
import torchvision.datasets as normal_datasets
import torchvision.transforms as transforms
from torch.autograd import Variable

#Data transformation
transform_=transforms.Compose([
    transforms.Resize((28, 28)),
    transforms.RandomVerticalFlip(),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])

# 将数据处理成Variable, 如果有GPU, 可以转成cuda形式
def get_variable(x):
    x = Variable(x)
    return x.cuda() if torch.cuda.is_available() else x

# Load some commonly used datasets from torchvision.datasets,
# If there is no local data, you can download it,just download=Ture
train_dataset = normal_datasets.MNIST(root='./mnist/',  train=True, transform=transform_, download=False)

train_loader = torch.utils.data.DataLoader(dataset=train_dataset,batch_size=64,shuffle=True)

test_dataset = normal_datasets.MNIST(root='./mnist/', train=False,transform=transform_,download=False)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,batch_size=64,shuffle=False)


# Defining a convolutional neural network
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.layer_1 = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=5,padding=2),#16,28,28
            nn.BatchNorm2d(16),
            nn.ReLU(inplace=True),

            nn.Conv2d(16,16,kernel_size=3),#16,26,26
            nn.BatchNorm2d(16),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2,stride=2)#16,13,13
        )
        self.layer_2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=5, padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Conv2d(32, 32, kernel_size=3, padding=0),#32,11,11
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3,stride=2)#32,5,5
        )
        self.fc = nn.Linear(5 * 5 * 32, 10)

    def forward(self, x):
        out = self.layer_1(x)
        out = self.layer_2(out)
        out = out.view(out.size(0), -1)  # reshape
        out = self.fc(out)
        return out

if torch.cuda.is_available():
    cnn = CNN().cuda()
else :cnn=CNN()

num_epochs = 10
learning_rate = 0.001

# Choose a loss function and optimization method
loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(cnn.parameters(), lr=learning_rate)

if __name__ == '__main__':
    print("Start train model\n")
    for epoch in range(num_epochs):
        for i, (images, labels) in enumerate(train_loader):
            images = get_variable(images)
            labels = get_variable(labels)

            outputs = cnn(images)
            loss = loss_function(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if (i + 1) % 100 == 0:
                print('Epoch [%d/%d], Iter [%d/%d] Loss: %.4f'% (epoch + 1, num_epochs, i + 1, len(train_dataset) // 64, loss.item()))

    # Save the Trained Model
    torch.save(cnn.state_dict(), './cnn.pkl')
    print("End train")