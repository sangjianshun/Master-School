class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def fun(self):  #实例方法
        self.day +=1

    @staticmethod  # 静态方法
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(year,month,day)

    @staticmethod  # 静态方法
    def valid_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year) > 0:
            return True
        else:
            return False

    @classmethod  # 类方法
    def from_string(cls,date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(year,month,day)

    # @classmethod  # 类方法
    # def from_string(cls,date_str):
    #     year, month, day = tuple(date_str.split("-"))
    #     return cls(year,month,day)

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"

if __name__ == '__main__':

    new_day = Date(2021, 4,7)
    new_day.fun()
    print(new_day)

    # 方法一，外面处理
    # 2021-4-7
    data_str = "2021-4-7"
    year,month,day = tuple(data_str.split("-"))
    new_day_1 = Date(year,month,day)
    print(new_day_1)

    # 方法二，静态方法
    new_day_2 = Date.parse_from_string(data_str)
    print(new_day_2)

    # 方法三，类方法
    new_day_3 = Date.from_string(data_str)
    print(new_day_3)
