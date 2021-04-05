a = {"t1":{"t11":11},
     "t2":{"t21":22}}
# clear
a.clear()
print(a)

# copy,返回浅拷贝
new_a = a.copy()

import copy
new_deep_a = copy.deepcopy(a)