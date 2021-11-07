# Python3 中有六个标准的数据类型：
# 
# Number（数字）
# 
# String（字符串）
# 
# List（列表）
# 
# Tuple（元组）
# 
# Set（集合）
# 
# Dictionary（字典）

## 1. 集合的创建
### 1.1 直接创建


set_master_school = {1, 2, "master", "school"}


### 1.2 通过set创建


set_master_school = set(("123")) # 注意，创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
set_master_school = set(("123",))




## 2. 增
### 2.1 add


set_master_school.add(3)



### 2.2 update


set_master_school.update("12") # 和集合定义一样，需要参数是可迭代的对象
set_master_school.update(("12")) # 和上面等价
set_master_school.update(("12",)) # 注意这个和上面的区别，上面是字符串，下面是tuple，当tuple只有一个元素时需注意
set_master_school.update(("12",),("1234")) # 可以有多个


## 3. 删
### 3.1 remove


set_master_school.remove("12") # 没有会报错


### 3.2 discard


set_master_school.discard("test") # 不会报错
set_master_school.discard("4")



### 3.3 pop


set_master_school.pop() #删除左边第一个元素，由于集合是无序的，所以是随机删除一个元素


### 3.4 clear


set_master_school.clear() # 清空


## 4. 改
# 无
## 5. 查
### 5.1 in


print("master" in set_master_school)

## 6. 集合的基本操作
### 6.1 差集


tmp_set = {1,2,3,4}
tmp_list = [1,2,3,4]
set_master_school = {1, 2, "master", "school"}

set_master_school.difference_update(tmp_set)

set_master_school = set_master_school.difference(tmp_set)

set_master_school = set_master_school - tmp_set

set_master_school.difference_update(tmp_list) # 是可迭代的对象即可
set_master_school = set_master_school - tmp_list # 注意减号和difference的区别

set_master_school = set_master_school - tmp_set


### 6.2 交集


tmp = {1,2,3,4}
set_master_school = {1, 2, "master", "school"}

set_master_school.intersection_update(tmp) # 可迭代的对象即可

set_master_school = set_master_school.intersection(tmp)

set_master_school = set_master_school & tmp



### 6.3 并集


tmp = {1,2,3,4}
set_master_school = {1, 2, "master", "school"}

set_master_school = set_master_school.union(tmp) # 并集没有update方法
set_master_school = set_master_school | tmp



### 6.4 对称差集


tmp = {1,2,3,4}
set_master_school = {1, 2, "master", "school"}

# set_master_school.symmetric_difference_update(tmp)

# set_master_school = set_master_school.symmetric_difference(tmp)

# set_master_school = (set_master_school | tmp) - (set_master_school & tmp)

set_master_school = set_master_school ^ tmp


## 7. 其他
### 7.1 copy


a = set_master_school.copy() # 和mylist中的copy方法一样
b = set_master_school # 最浅的拷贝
set_master_school.add(10)



### 7.2 isdisjoint


tmp = {1,2,3,4}
set_master_school = {1, 2, "master", "school"}
print(set_master_school.isdisjoint(tmp)) # 如果joint返回False，如果没有交集返回True



### 7.3 issubset


tmp = {1,2}
set_master_school = {1, 2, "master", "school"}
print(tmp.issubset(set_master_school)) #是子集，返回True



### 7.4 issuperset


tmp = {1,2}
set_master_school = {1, 2, "master", "school"}
print(set_master_school.issuperset(tmp)) #是子集，返回True，注意和issubset的区别


print(1)



