a = 9999999999999999999999999999999999999
b = 9999999999999999999999999999999999999
print(a is b)  # True，小整数时，python会将他们放在同一个内存空间，这是python的一个优化机制
print(a == b)  # True
print(id(a))
print(id(b))

a = c = [1, 2]
b = [1, 2]
print(a is b)  # False
print(a == b)  # True
print(a is c)  # True
print(id(a))   # a和c的id一样
print(id(b))
print(id(c))
