class MyClass():
    def __init__(self, var):
        self.__var = var # 私有属性，无法通过实例访问，可以通过公共方法访问



if __name__ == '__main__':
    myClass = MyClass("test")
    # print(myClass.__var) # AttributeError: 'MyClass' object has no attribute '__var'

    print(myClass._MyClass__var) # 这种方式也可以拿出来变量的属性