def t_fun(name = "t_fun"):
    print(name)

class t_class():
    def __init__(self):
        print("t_class")

# 1.1 赋值给一个变量

# para_fun = t_fun
# para_fun("para_fun")
#
# # 括号进行了初始化
# para_clas = t_class
# para_fun()

# 1.2 可以添加到集合对象中
#
# t_list = []
# t_list.append(t_fun)
# t_list.append(t_class)
# for item in t_list:
#     print(item())

# 1.3 可以作为参数传递给函数, 可以当做函数的返回值
def dec_fun():
    print("dec_fun")
    return t_fun
para_fun = dec_fun()
para_fun()
