# python的变量实质上是一个指针 int str，也可以理解为一个便利贴(可以贴在任何地方，int str)

a = 1
# a贴在1上
# 先生成对象，然后贴便利贴

a = [1,2,3]
b = a
# b和a贴在同一个便利贴
print(a is b)
b.append(4)
print(a)