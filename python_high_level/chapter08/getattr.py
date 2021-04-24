# __getattr__、__getattribute__

# __getattr__在查找不到属性时调用

from datetime import date,datetime


class User:
    def __init__(self, name, birthday,info = {}):
        self.name = name
        self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        print("not find attr") # 这里可以做纠正
        return self.info[item]

    # 无论是否找到该属性，均先到下面这个函数
    # def __getattribute__(self, item): #尽量不使用，写不好就崩溃了，控制属性的访问过程
    #     return "t2"

if __name__ == '__main__':
    user = User("t1", date(year = 1994, month = 1, day = 1), info = {"t1":"t2"})
    print(user.age) # 查找不到属性时，调用魔法函数__getattr__
    print(user.t1)

