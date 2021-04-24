# 列表推导式
# 提取1-20之间的奇数
# 方法一
odd_list = []
for i in range(21):
    if i % 2==1:
        odd_list.append(i)
print(odd_list)

# 方法二
odd_list = [i for i in range(21) if i % 2 == 1]
print(odd_list)

# 列表生成式性能高于列表操作
def hand_item(item):
    return item * item
odd_list = [hand_item(i) for i in range(21) if i % 2 == 1]
print(odd_list)

# 生成器表达式
odd_gen = (i for i in range(21) if i % 2 == 1) # 变成一个生成器
print(type(odd_gen)) # <class 'generator'>
print(odd_gen)  # 生成器地址

odd_list = list(odd_gen)
print(type(odd_list)) # <class 'list'>
print(odd_list)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 字典推导式
my_dict = {"k1":22,"k2":23,"k3":24}
reverse_dict = {value:key for key,value in my_dict.items()}
print(reverse_dict)

# 集合推导式
my_set = {key for key,value in my_dict.items()} # 等价于my_set = set(my_dict.key())
print(type(my_set))
print(my_set)
