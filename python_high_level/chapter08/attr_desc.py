import numbers
from datetime import date,datetime

class IntField:
    # 以下方法只实现一个方法就是属性描述符
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value

    def __delete__(self, instance):
        pass

class NoneDataIntField():
    # 非数据描述符
    def __get__(self, instance, owner):
        return self.value


class User:
    age = IntField() #age是一个属性描述符

if __name__ == '__main__':
    user = User()
    user.__dict__["age"] = 10
    print(user.__dict__)
    print(user.age)  # 注意user.age和user__dict__是不一样的

    print(getattr(user,'age')) # 与print(user.age)等价
    # 首先调用__getattribute__, zuihou shi

    # 顺序：
    # 1、属性在类中且属性是数据描述符，比如
    # class User:
    #     age = IntField() #age是一个属性描述符

    # 2、属性在对象的__dict__中，直接返回obj.__dict__['age']
    # class User:
    #     age = IntField() #age是一个属性描述符

    ## 3、属性在类中，age是一个非数据描述方法，返回__get__方法的结果
    # class User:
    #     age = NoneDataIntField()

    ## 4、属性在类中，age不是一个非数据描述方法，返回__dict__['age']
    # class User:
    #     age = 1

    ## 5、User有__getattr__方法，调用__getattr__的结果
    # class User:
    #     def __getattr__(self, item):
    #         return item
