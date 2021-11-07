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

## 1. 字典的创建
### 1.1 直接创建
dict_master_school = {1:2, "name":"master school"}
dict_master_school = {} # 空字典

### 1.2 通过dict创建
dict_master_school = dict(name = "master school") # 这种方式key不能是整数
dict_master_school = dict([[1, 2], ('name', "master school")]) # 通过可迭代的对象创建
dict_master_school = dict(((1, 2), ('name', "master school")))
dict_master_school = dict(zip([1, "name"], [2, "master school"]))  # zip([a,b],[c,d])和上面等价
# dict_master_school = dict.fromkeys([1, "name"],[2, "master school"]) # 这种方式value只能设置一个默认值

## 2. 增
### 2.1. 直接增加
dict_master_school[2] = 3
### 2.2. update
dict_master_school_tmp = {1:10, 10:1}
dict_master_school.update(dict_master_school_tmp) # 合并两个dict，如果key相同则更新value
## 3. 删
### 3.1. del
# del dict_master_school[2]
# del dict_master_school
### 3.2. clear
# dict_master_school.clear()
### 3.3. pop
dict_master_school.pop(10)

### 3.4. popitem()
dict_master_school.popitem() # 和pop的区别在于，pop必须要指定key，这个是删除最后一个items。具有随机性

## 4. 改
dict_master_school[1] = 3

## 5. 查
### 5.1. 直接查
print(dict_master_school["name"])
### 5.2. get
value = dict_master_school.get(10, 100)
### 5.3. setdefault(key, default=None)
value = dict_master_school.setdefault(10, 100) #比get多做一步，如果没有的情况下，进行添加
## 6. 其他
### 6.1. copy
dict_master_school_copy = dict_master_school.copy()
dict_master_school_tmp = dict_master_school
dict_master_school[1] = 100

### 6.2. items
items = dict_master_school.items() # 可迭代的对象
for key, value in items:
    print(key,value)

### 6.3. keys
keys = dict_master_school.keys()
for key in keys:
    print(key)

### 6.4. values
values = dict_master_school.values()
for value in values:
    print(value)

print(1)