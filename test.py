from PIL import Image
from torchvision import transforms
from torch.autograd import Variable
import torch
import torch.nn as nn
import torchvision.datasets as dset
import random

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

def get_result(root=None):

######Get the trained neural network model here#######
    model = CNN()
    if torch.cuda.is_available():
        model.cuda()
    model.load_state_dict(torch.load('./cnn.pkl'))
##########################end########################

##Randomly get data from subfolders in root folder###
    folder_dataset = dset.ImageFolder(root=root)
    img0_tuple = random.choice(folder_dataset.imgs)
    get_transform=transform
    data = Image.open(img0_tuple[0]).convert('L')
    data = get_transform(data)
    data = Variable(data.unsqueeze(0))
##############And transform the data################

    output = model(data)
    _, predit = torch.max(output, 1)
    return  predit.numpy()[0] , img0_tuple[0],img0_tuple[1]


transform = transforms.Compose([
                                transforms.Resize((28,28)),
                                transforms.ToTensor(),
                                transforms.Normalize([0.5], [0.5])
                                ])


if __name__ == '__main__':
    result,_,num=get_result(root='C:/Users\FDL\Desktop/test/')
    print(result)
    print(_)




