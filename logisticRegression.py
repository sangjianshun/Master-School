import numpy as np
def sigmoid(z):
    return 1/(1+np.exp(-z))

def LR(x,w,b):
    return sigmoid(w*x[j] + b)

def BP(x,y,epoch = 10, eta = 0.001):
    w = 0.1
    b = 0.1
    for i in range(epoch):
        for j in range(len(x)):
            fx = LR(x,w,b)
            w = w - eta * (fx - y[j])*x[j]
            b = b - eta * (fx - y[j])
    return w,b
