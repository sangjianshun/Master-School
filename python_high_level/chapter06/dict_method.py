# dict中的一些自带的函数
a = {"t1":{"t11":11},
     "t2":{"t21":22}}
# clear
a.clear()
print(a) # {}

# fromkeys
a = ["t1","t2"]
new_dict = dict.fromkeys(a, {"t11":11})
print(new_dict) # {'t1': {'t11': 11}, 't2': {'t11': 11}}

# get
print(new_dict.get("t3",{})) #如果取值不到，返回是空

# setdefault
print(new_dict)
value_test = new_dict.setdefault("t4", "t4") #setdefualt的步骤实际上要比自己判断有没有key然后没有加入key，设置value的步骤要少一些
print(new_dict)
print(value_test) # t4

# update
# 方法一
# new_dict.update({"t5":"t5", "t6":"t6"})
# 方法二，注意key没有双引号
# new_dict.update(t5="t5", t6="t6")
# 方法三，注意是list中放了tuple
new_dict.update([("t5","t5"), ("t6","t6")])
# 方法四，tuple和list是等价的，两个list也可以换成两个tuple
new_dict.update([["t5","t5"], ["t6","t6"]])
print(new_dict) # {'t1': {'t11': 11}, 't2': {'t11': 11}, 't4': 't4', 't5': 't5', 't6': 't6'}

# 浅拷贝
a = {"t1":{"t11":11},
     "t2":{"t21":22}}
# copy,返回浅拷贝
new_a = a.copy()
new_a["t1"]["t11"] = 33 # 之前的字典也随之改变
print(a) # {'t1': {'t11': 33}, 't2': {'t21': 22}}

#深拷贝
import copy
a = {"t1":{"t11":11},
     "t2":{"t21":22}}
new_deep_a = copy.deepcopy(a)
new_deep_a["t1"]["t11"] = 33 # 之前的字典不会改变
print(a)  # {'t1': {'t11': 11}, 't2': {'t21': 22}}