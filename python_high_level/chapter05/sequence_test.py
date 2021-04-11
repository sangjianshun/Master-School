my_list = []
my_list.append(1)
my_list.append("a")

from collections import abc

b = [3, 4]

# list + list
a = [1, 2]
a = a + b # a=[1, 2, 3, 4]

# list += list
a = [1, 2]
a += b # a=[1, 2, 3, 4]

# list.extend(list)
a = [1, 2]
a.extend(b) # a=[1, 2, 3, 4]



b = (3,4)

# list + tuple 报错
# a = [1, 2]
# a = a + b # TypeError: can only concatenate list (not "tuple") to list

# list += tuple
a = [1, 2]
a += b # a=[1, 2, 3, 4]

# list.extend(tuple)
a = [1, 2]
a.extend(b) # a=[1, 2, 3, 4]


a =(1,2)
b =(3,4)
a = a+b
print(a)
# b = a + [3,4]
# print(b) #[1, 2, 3, 4]

# a += [3, 4]
# print(a)  # [1, 2, 3, 4]
#
# a += (3, 4)  # [1, 2, 3, 4]
# b = a + (3, 4)  # TypeError: can only concatenate list (not "tuple") to list

# 以下是序列类型的协议
# "Sequence", "MutableSequence",

# class Sequence(Reversible, Collection):

# class Collection(Sized, Iterable, Container):

# class MutableSequence(Sequence):
#
#     __slots__ = ()
#
#     """All the operations on a read-write sequence.
#
#     Concrete subclasses must provide __new__ or __init__,
#     __getitem__, __setitem__, __delitem__, __len__, and insert().
#
#     """
#
#     @abstractmethod
#     def __setitem__(self, index, value):
#         raise IndexError
#
#     @abstractmethod
#     def __delitem__(self, index):
#         raise IndexError
