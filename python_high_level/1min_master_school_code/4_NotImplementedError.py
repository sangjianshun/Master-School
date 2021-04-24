# 第一种方式
# class BaseClass():
#     def fun(self, x):
#         print(x)
#         raise NotImplementedError
#
# class ObjClass(BaseClass):
#     pass
#
# objClass = ObjClass()
# objClass.fun("test") # NotImplementedError

# # 第二种方式，使用抽象基类，优点，未调用该子函数时就会报问题，前面只要不调用子函数，就不会报错。强约束
# import abc
# # 模拟抽象基类
# class BaseClass(metaclass=abc.ABCMeta):
#     @abc.abstractmethod  # 修饰器
#     def fun(self, x):
#         print(x)
#         pass
#
# class ObjClass(BaseClass):
#     pass
#
# objClass = ObjClass() # TypeError: Can't instantiate abstract class ObjClass with abstract methods fun
# objClass.fun("test")

