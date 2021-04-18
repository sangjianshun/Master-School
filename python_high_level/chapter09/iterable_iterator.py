from collections.abc import Iterator
class Company():
    def __init__(self, employee_list):
        self.employee = employee_list
    def __iter__(self):  # 自己定义迭代器时，一般不自己实现next函数，而是采用这种方法。
        return MyIterator(self.employee)
    def __getitem__(self, item):
        return self.employee[item]

class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0
    def __next__(self):
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

if __name__ == '__main__':
    company = Company(["t1", 't2'])
    my_iter = iter(company) # 优先考虑__iter__如果没有再看__getitem__
    for item in my_iter:
        print(item)

    for item in company:
        print(item)