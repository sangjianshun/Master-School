# list是动态的,大小可变即长度可变的数组
# 存放的实际上是对象的引用，因此可以存放不同类型的数据

## 1.1 list的创建
### 1.1.1 直接创建
list_master_school = [1, 2, "master", "school"]
### 1.1.2 通过list创建
list_master_school = list((1, 2, "master", "school"))  # 将一个可迭代的对象变成list,tuple是一个可迭代的对象
## 1.2 增
### 1.2.1 append
list_master_school.append(3)  # [1, 2, 'master', 'school', 3]
list_master_school.append([1, 2])  # [1, 2, 'master', 'school', 3, [1,2]]

### 1.2.2 extend,+,+=
list_master_school.extend(["e1", "e2"])  # [1, 2, 'master', 'school',3 , [1,2],"e1","e2"]，注意参数可迭代即可，和+=等价，和+逻辑不一样
list_master_school += ("e1", "e2")  # 这里是可迭代即可
list_master_school = list_master_school + ["e1", "e2"]  # [1, 2, 'master', 'school', 3, [1,2],"e1","e2"] 注意这里必须是list
list_master_school = ["master school"] * 3
### 1.2.3 insert
list_master_school.insert(1, 10)
## 1.3 删
### 1.3.1 remove
list_master_school.remove([1, 2])  # [1, 10, 2, 'master', 'school', 3, 'e1', 'e2'] 如果没有会报错，只会删除找到的第一个
### 1.3.2 pop
list_master_school.pop(-2)
x = list_master_school.pop()  # Remove and return item at index (default last)，删除索引对应的元素
### 1.3.3 del
del list_master_school[0]
del list_master_school[1:3]  # 也可以删除切片
# del list_master_school  # 注意和clear的区别，clear是清空，这个是删除这个变量
### 1.3.4 clear
# list_master_school.clear()  # 清空

## 1.4 改
list_master_school[3] = 1
## 1.5 查
### 1.5.1 切片
a = list_master_school[1:]
b = list_master_school[:5]
c = list_master_school[:5:3]
### 1.5.2 直接访问
d = list_master_school[1]
### 1.5.3 查索引index
e = list_master_school.index(3)
e = list_master_school.index(3, 1, 100)  # 寻找范围缩小为子list
## 1.6 其他
### 1.6.1 sort
list_master_school = [1, 3, 2, 6, 5]
list_master_school_index = [2, 1, 3, 0, 4]
sorted_index = sorted(list_master_school_index, key=lambda i: list_master_school[i])  # 这种方法不改变原list，会产生新的list
list_master_school_index.sort(key=lambda i: list_master_school[i])
list_master_school.sort()  # key=lambda x:x默认值

### 1.6.2 reverse
list_master_school.reverse()
### 1.6.3 max,min
max_val = max(list_master_school)
### 1.6.4 count
count_num = list_master_school.count(1)
### 1.6.5 copy
# copy是浅度复制，修改列表不会互相影响，但是修改列表里面的对象会影响
list_master_school = [1, 3, 2, 6, 5]
list_master_school_copy = list_master_school
list_master_school[0] = 100  # list_master_school_copy会随之改变

list_master_school = [{'name': "master"}, 1, 3]
list_master_school_copy = list_master_school.copy()
list_master_school[0]["name2"] = "school"  # list_master_school_copy会改变
list_master_school[1] = 100  # list_master_school_copy不会改变

print(1)
