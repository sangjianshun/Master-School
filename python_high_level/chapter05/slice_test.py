test_list = [3,4,2,1,2,4,5,6]
print(test_list[::]) # 返回和test_list一样的新列表
print(test_list[::-1]) # 此处start = len(test_list)-1, end = -1
print(test_list[:100]) # end > len(test_list) 截断
print(test_list[100:]) # 返回空列表

test_list[len(test_list):] = [100,200] # 有点像分片后赋值 test_list = [3, 4, 2, 1, 2, 4, 5, 6, 100,200]
test_list[3:3] = [1000] # 插入元素 test_list = [3, 4, 2, 1000, 1, 2, 4, 5, 6, 100, 200]

test_list[::2] = [0] * len(test_list[::2]) # 注意等号左右两边长度必须相等test_list = [0, 4, 0, 1000, 0, 2, 0, 5, 0, 100, 0]
test_list[:5] = []  # 删除前五个元素，等价于del test_list[:5], test_list = [2, 0, 5, 0, 100, 0]
