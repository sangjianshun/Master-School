
# 类变量和对象变量的区别
class A:
    aa = 1 # 类变量
    def __init__(self,x,y):
        self.x = x
        self.y = y

a = A(1,2)
A.aa = 111  # 类变量
a.aa = 100  # 对象变量，实例a会被赋值给a.aa，此时A的类变量不变
print(a.x, a.y, a.aa)
print(A.aa)
# print(A.x) # type object 'A' has no attribute 'x'

b = A(4,5)
print(b.aa) # 111