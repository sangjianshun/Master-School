# Variable, Tensor 和 parameter之间的区别

# tensor和numpy一样，是pytorch里面的一种数据结构
# Variable默认不计算梯度，在使用.step()更新参数时，需要在优化器中手动加入该参数，因为不会被自动封装到model.parameter()之中
# Parameter默认计算梯度，在使用.step()更新参数时，会自动更新参数。另外说明，model.parameter()是一个生成器。
# optimizer = torch.optim.SGD(list(model.parameters()) + [model.weight], lr=1e-6)

import torch
a = torch.randn((1,1))  # tensor
b = torch.randn((1,1))

a1 = torch.nn.Parameter(a)
b1 = torch.autograd.Variable(b) # 默认是不需要计算梯度的。感觉和Parameter之间的一个区别是默认不计算梯度
c = a1 + b1

# 通过调用backward()，我们可以对Variable进行一次自动求导
c.backward()
c.backward()
# a1 = a1 - a1.grad

SGD = torch.optim.SGD([b1, c], lr = 1)  # C: 没有梯度，non-leaf Tensor，不可以加入到parameter之中
SGD.zero_grad()
c.backward()
SGD.step()
print(1)