from datetime import date,datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0  # 这个属性不想对外暴露，一种代码规范，虽然外部也可以访问

    # def get_age(self):
    #     return datetime.now().year - self.birthday.year

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self,value):
        self._age = value
if __name__ == '__main__':
    user = User("t1", date(year = 1994, month = 1, day = 1))
    print(user.age) # 调用了@property

    user.age = 90 # 调用了@age.setter
    print(user._age)