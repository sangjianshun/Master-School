from python_high_level.chapter04.class_method import Date


class User:
    def __init__(self, birthday):
        self.__birthday = birthday # 私有属性，无法通过实例访问，可以通过公共方法访问

    def get_age(self):
        return 2018 - self.__birthday.year


if __name__ == '__main__':
    user = User(Date(2000,1,1))
    # print(user.birthday) # AttributeError: 'User' object has no attribute 'birthday'
    print(user.get_age())

    print(user._User__birthday) # 这种方式也可以拿出来变量的属性