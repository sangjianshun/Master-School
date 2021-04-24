class MyClass:
    def __init__(self, num):
        self.num = num

    def fun(self):  #对象方法
        self.num +=1

myClass = MyClass(10)
myClass.fun()
print(myClass.num)

class MyClass:
    def __init__(self, num):
        self.num = num

    @staticmethod  # 静态方法
    def fun(var):  # 静态方法不需要传self
        var += 1
        return var
myClass = MyClass(10)
myClass.num = myClass.fun(myClass.num)
print(myClass.num)



class MyClass:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod  # 类方法
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(year,month,day)
    def __str__(self):
        return str(self.year) + str(self.month) + str(self.day)

data_str = "2021-12-10"
myClass = MyClass.from_string(data_str)
print(myClass)
