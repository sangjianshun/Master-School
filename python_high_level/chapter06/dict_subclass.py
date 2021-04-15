#不建议继承list和dict等
class Mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key,value*2)

my_dict = Mydict(one = 1)
print(my_dict) # {'one': 1}并没有调用自定义的魔法函数

my_dict["one"] = 1
print(my_dict) # {'one': 2} 调用了自定义的魔法函数

from collections import UserDict

class Mydict2(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key,value*2)
my_dict2 = Mydict2(one = 1)
print(my_dict2) # {'one': 2}

from collections import defaultdict

my_dict3 = defaultdict(dict)  # 其实是实现了__missing__的魔法函数
my_value = my_dict3["tt"]
print(my_value)


