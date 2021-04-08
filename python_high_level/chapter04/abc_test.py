# 检查某个类是否有某种方法

class School():
    def __init__(self,teacher_list):
        self.teacher = teacher_list
    def __getitem__(self, item):
        return self.teacher[item]
    def __len__(self):
        return 1000000
    def __repr__(self):
        return "repre hello world"

sch = School(["boby1", "boby2"])

# 判断是否有这个函数
print(hasattr(sch, "__len__"))

from collections.abc import Sized
print(isinstance(sch, Sized))


import abc
# 模拟抽象基类
class BaseScrapy(metaclass=abc.ABCMeta):
    @abc.abstractmethod  # 修饰器
    def fun(self, x):
        print(x)
        pass

class AScrapy(BaseScrapy):
    pass

aScrapy = AScrapy()
aScrapy.fun("test")
