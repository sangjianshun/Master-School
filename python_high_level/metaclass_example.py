# 类 + 括号得到一个对象【执行__new__和__init__】
# 为什么是执行这个，实际上是去执行的type.__call__方法（因为他是type创建的一个对象，相当于执行__CALL__方法），只不过type.__call__方法是要求先去执行__NEW__然后去执行的__INIT__方法。

# 对象 + 括号 【执行__call__方法】

# 示例一：__init__和__new__的区别
# class MyClass():
#     def __init__(self,name):
#         print("MyClass.__init__") # 2:MyClass.__init__
#         self.name = name # 3
# myClass = MyClass("master school") # 1
# print(myClass.name) # 4:master school


# 1:实际上是去执行的type.__call__方法（因为MyClass是type创建的一个对象，相当于执行__CALL__方法），
# 只不过type.__call__方法是要求先去执行__NEW__然后去执行的__INIT__方法。
# class MyClass():
#     def __init__(self,name):
#         print("MyClass.__init__") # 4:MyClass.__init__
#         self.name = name # 5
#     def __new__(cls, *args, **kwargs):
#         print("MyClass.__new__") # 2:MyClass.__new__
#         return super(MyClass, cls).__new__(cls) # 3
# myClass = MyClass("master school")  # 1
# print(myClass.name) # 6:master school


# # 示例二：研究自定义类的底层原理
# class MyClass():
#     def __init__(self,name):
#         print("MyClass.__init__")
#         self.name = name
# myClass = MyClass("master school")
# print(type(myClass)) # <class '__main__.MyClass'>
# print(type(MyClass)) # <class 'type'>
# print(myClass) # <__main__.MyClass object at 0x000001F66FD1B220>
# print(MyClass) # <class '__main__.MyClass'>
# print(myClass.name) # master school
#
# def __init__(self, name):
#     self.name = name
# MyClass2 = type("MyClass2", (), {'__init__': __init__})
# myClass2 = MyClass2("master school")
# print(type(myClass2)) # <class '__main__.MyClass2'>
# print(type(MyClass2)) # <class 'type'>
# print(myClass2) # <__main__.MyClass2 object at 0x000001F66FD4E550>
# print(MyClass2) # <class '__main__.MyClass2'>
# print(myClass2.name) # master school

# 示例三：使用metaclass创建类
# class MyMetaClass(type):
#     def __init__(self, *args, **kwargs):
#         print("MetaClass.__init__")
#         super().__init__(*args, **kwargs)
#     def __new__(cls, *args, **kwargs):
#         print("MetaClass.__new__")
#         new_class = super().__new__(cls,*args, **kwargs)
#         print(new_class)
#         return new_class
#
# # MyClass 由元类MyMetaClass来创建
# # MyClass是一个对象，由MyMetaClass来创建
# # 在使用MyMetaClass创建类的过程中，也是遵循先执行__new__后执行__init__
# class MyClass(metaclass=MyMetaClass):
#     print("MyClass")
#     pass
#
# print("debug")
# MyClass2 = MyMetaClass("MyClass2", (), {})


# # 示例四：__call__方法
# class MyClass():
#     def __init__(self, name):
#         print('MyClass.__init__')
#         self.name = name
#     def __call__(self, x):
#         print("MyClass.__call__")
#         print(x)
#         print(self.name)
#
# myClass = MyClass("master school")
# myClass("test")


# # 示例五：元类中的__call__方法
# class MyMetaClass(type):
#     def __init__(self, *args, **kwargs):
#         print("MetaClass.__init__")
#         super().__init__(*args, **kwargs)
#     def __new__(cls, *args, **kwargs):
#         print("MetaClass.__new__")
#         new_class = super().__new__(cls,*args, **kwargs)
#         print(new_class)
#         return new_class
#
#     def __call__(self, *args, **kwargs):
#         print('MetaClass.__call__')
#         # 1. 调用自己那个类的__new__方法去创建对象
#         obj = self.__new__(self)
#         # 2. 调用自己哪个类的__init__方法去初始化
#         self.__init__(obj, *args, **kwargs)
#         return obj
#
# class MyClass(metaclass=MyMetaClass):
#     def __init__(self, name):
#         print('MyClass.__init__')
#         self.name = name
#
#     def __new__(cls, *args, **kwargs):
#         print('MyClass.__new__')
#         return object.__new__(cls)
# print("debug")
# # MyClass("master school") 可以理解为 类+()
# # 也可以理解为由MyMetaClass创建的对象+括号
# # 优先会执行__call__方法
# # 注意， MyClass("master school")这里没有运行MyMetaClass的__new__方法和__init__方法
# myClass = MyClass("master school")
print(1)
###########   示例结束
