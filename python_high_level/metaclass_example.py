class MetaClass(type):
    def __init__(self, name, bases, dic):
        super().__init__(name, bases, dic)
        print("MetaClass.__init__")
    def __new__(cls, *args, **kwargs):
        print('MetaClass.__new__')
        return type.__new__(cls, *args, **kwargs)
    def __call__(cls, *args, **kwargs):
        print('MetaClass.__call__')
        obj = cls.__new__(cls)
        cls.__init__(cls, *args, **kwargs)
        return obj
#
# class MyClass(metaclass=MetaClass):
#     def __init__(self, name):
#         print('MyClass.__init__')
#         self.name = name
#
#     def __new__(cls, *args, **kwargs):
#         print('MyClass.__new__')
#         return object.__new__(cls)
#
# print("debug")
# myClass = MyClass("myClass")
# print(1)





# class MyClass():
#     num = 100
# myClass = MyClass()
# print(type(myClass)) # <class '__main__.MyClass'>
# print(type(MyClass)) # <class 'type'>
#
# print(myClass, MyClass) # <__main__.MyClass object at 0x0000022369DADDC0> <class '__main__.MyClass'>
#
#
# # class = type(classname, superclasses, attributedict)
# # type(classname, superclasses, attributedict)，就是 type 的 __call__ 运算符重载，它会进一步调用：
# # type.__new__(typeclass, classname, superclasses, attributedict)
# # type.__init__(class, classname, superclasses, attributedict)
#

MyClass2 = MetaClass("MyClass2", (), {"num":100}) #
print("debug")
myClass2 = MyClass2()
print(myClass2, MyClass2)
print(myClass2.num)

