# 什么是迭代协议
# 迭代器是访问集合内元素的一种方式，一般用来便利数据
# 迭代器和以下标的访问方式不一样，迭代器是不能返回的，提供了一种惰性方式数据的方式
# 实现魔法函数 __iter__变成可迭代对象
# 再实现魔法函数 __next__变成迭代器

from collections.abc import Iterable,Iterator
a = []
print(isinstance(a, Iterable))
print(isinstance(a,Iterator)) # False