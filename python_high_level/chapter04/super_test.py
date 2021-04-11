class A:
    def __init__(self):
        print("a")

class B(A):
    def __init__(self):
        print("b")
        super().__init__()  #super(B, self).__init__()

class C(A):
    def __init__(self):
        print("c")
        super(C, self).__init__()
class D(B,C):
    def __init__(self):
        print("d")
        super(D, self).__init__()

if __name__ == '__main__':
    # b = B()
    d = D() # d,b,c,a 注意这里b后面是c不是a
    print(D.__mro__) # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)