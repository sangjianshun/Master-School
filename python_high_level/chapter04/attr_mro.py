class A:
    name = "A"  # 类属性
    def __init__(self):
        self.name = "obj"  # 对象属性

a = A()
print(a.name)
print(A.name)

# C3算法
# class D:
#     pass
# class C(D):
#     pass
# class B(D):
#     pass
# class A(B,C):
#     pass
# print(A.__mro__) # (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)


class D:
    pass
class E:
    pass
class C(E):
    pass
class B(D):
    pass
class A(B,C):
    pass
print(A.__mro__) # (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class 'object'>)

