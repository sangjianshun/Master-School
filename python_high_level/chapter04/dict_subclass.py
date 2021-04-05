# class Mydict(dict):
#     def __setitem__(self, key, value):
#         super().__setitem__(key,value*2)
#
# # 这两种方式结果不一样
# my_dict = Mydict(one=1)
# my_dict["one"] = 1
# print(my_dict)

from collections import UserDict
class Mydict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key,value*2)
my_dict = Mydict(one=1)
print(my_dict)

from collections import defaultdict