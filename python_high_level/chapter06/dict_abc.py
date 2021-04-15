from collections import Collection
from collections.abc import Mapping,MutableMapping

# dict属于mapping类型,dict并没有继承mapping，只是因为他实现了mapping中的一些魔法函数。

#继承关系是MutableMapping继承了mapping，mapping继承了collections
a = {}
print(isinstance(a, MutableMapping))
print(isinstance(a, Mapping))
print(isinstance(a,  Collection))
