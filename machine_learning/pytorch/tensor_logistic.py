import torch
import math

# x = torch.linspace(-math.pi+1, math.pi+1, 2000)
# y = [0] * 1000 + [1] * 1000
from sklearn import datasets
dataset = datasets.load_iris()
x = []
y = []
for i in range(len(dataset.data)):
    if dataset.target[i] < 2:
        x.append(dataset.data[i].tolist())
        y.append(float(dataset.target[i]))


class LogisticRegression(torch.nn.Module):
    def __init__(self):
        """
        """
        super().__init__()

        self.weight = torch.nn.Parameter(torch.randn((4, 1)))
        self.bias = torch.nn.Parameter(torch.randn(()))

    def forward(self, x):
        """
        In the forward function we accept a Tensor of input data and we must return
        a Tensor of output data. We can use Modules defined in the constructor as
        well as arbitrary operators on Tensors.
        """
        # z = self.weight * x + self.bias
        z = torch.matmul(x, self.weight) + self.bias
        y = torch.sigmoid(z)
        # y = 1/(1 + torch.exp(-z))
        y1 = 1 - y
        logits = torch.cat((y, y1), -1)
        return logits

    def __str__(self):
        return f'simoid({self.weight.item}x + {self.bias})'
logisticRegression = LogisticRegression()
loss_fn = torch.nn.CrossEntropyLoss()
# optimizer = torch.optim.SGD(logisticRegression.parameters(), lr=0.0001)
optimizer = torch.optim.Adam(logisticRegression.parameters(), lr=0.0001)
#
for i in range(100):
    for i in range(len(x)):
        input = x[i]
        input = torch.tensor(input)
        input = torch.unsqueeze(input, dim= 0)

        label = torch.tensor(y[i])
        label = torch.unsqueeze(label, dim= -1)
        label = label.long()
        predict = logisticRegression(input)
        loss = loss_fn(predict, label)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(str(logisticRegression))
    print(loss.item())

for i in range(len(x)):
    input = x[i]
    input = torch.tensor(input)
    input = torch.unsqueeze(input, dim= 0)

    label = torch.tensor(y[i])
    label = torch.unsqueeze(label, dim= -1)
    label = label.long()
    predict = logisticRegression(input)
    predict = torch.argmax(predict).item()
    print(predict,label.item())




# from sklearn.linear_model import LogisticRegression
# lr = LogisticRegression(penalty= 'l2', solver='newton-cg',multi_class='multinomial')
# lr.fit(x,y)
# pred = lr.predict(x)
# for i in range(len(pred)):
#     print(pred[i], y[i])
# print(1)


