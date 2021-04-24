def add(a,b):
    a += b
    return a

# 传递一个list到函数中时，这个list很有可能会被改变
class Company:
    def __init__(self,name,staffs=[]):
        self.name = name
        self.staffs = staffs
    def add(self, staff_name):
        self.staffs.append(staff_name)
    def remove(self,staff_name):
        self.staffs.remove(staff_name)

if __name__ == '__main__':
    c1 = Company("c1",["t1","t2"])
    c1.add("t3")
    c1.remove("t1")
    print(c1.staffs)

    print(Company.__init__.__defaults__)

    c2 = Company("c2")
    c2.add("tt1")

    c3 = Company("c3")
    c3.add("ttt1")
    print(c2.staffs)
    print(c3.staffs)

    # 使用了默认值，同一个对象
    print(c2.staffs is c3.staffs)



    # a = 1
    # b = 2
    # c = add(a,b)
    # print(c)
    # print(a,b)
    #
    # a = [1,2]
    # b = [3,4]
    # c = add(a,b)
    # print(c)
    # print(a,b)
    #
    # a = (1,2)
    # b = (3,4)
    # c = add(a,b)
    # print(c)
    # print(a,b)