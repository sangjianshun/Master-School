# def create_class(name):
#     if name == 'user':
#         class User:
#             def __str__(self):
#                 return "user"
#         return User
#     elif name == 'company':
#         class Company:
#             def __str__(self):
#                 return "company"
#         return Company
#
# type动态创建类
def say(self):
    return self.name
class BaseClass:
    def answer(self):
        return "base class"
User = type("User", (BaseClass,), {"name":"user", "say":say})

# 元类是创建类的类，type实际上就是元类，因此对象是由class创建的，class是由type创建的（type是元类）


class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
# python中类的实例化过程，会首先寻找metaclass，通过metaclass去创建user类
# type去创建类对象

if __name__ == '__main__':
    # MyClass = create_class("user")
    # my_obj = MyClass()
    # print(type(my_obj))


    my_obj = User("test")
    print(type(my_obj))
    print(my_obj)
    # print(my_obj.name)
    # print(my_obj.say())
    # print(my_obj.answer())
