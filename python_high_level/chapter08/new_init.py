class User:
    # 在对象生成之前，控制对象的生成过程
    def __new__(cls, *args, **kwargs):
        print("in new")
        return super().__new__(cls)
    # 用来完善对象,如果new不返回对象，则不会调用init函数
    def __init__(self, name):
        print("in init")
        self.name = name


if __name__ == '__main__':
    user = User("test")