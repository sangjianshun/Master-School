# python中垃圾回收的算法是采用引用计数
a = 1
b = a

del a


# python中垃圾回收的算法是采用引用计数
a = object()

b = a
del a

print(b)
print(a)  # NameError: name 'a' is not defined