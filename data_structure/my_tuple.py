# tuple大小不可变

## 1. 元组的创建
### 1.1 直接创建
tuple_master_school = (1, 2, "master", "school")
tuple_master_school = () # 空元组
tuple_master_school = (1,) # 注意只有一个元素时必须要加逗号，否则括号表示运算符
tuple_master_school = 1, 2, "master", "school"


### 1.2 通过tuple创建
tuple_master_school = tuple("master") # 字符串是一个可迭代的对象
tuple_master_school = tuple(("master")) # 这个和上面是等价的，注意和下面的区别
tuple_master_school = tuple(("master",))
tuple_master_school = tuple([1, 2, "master", "school"]) # 将一个可迭代的对象变成tuple,list是一个可迭代的对象
tuple_master_school = tuple([1, 2, "master", "school"])

## 2. 增
# 无
## 3. 删
### 3.1 del
# del tuple_master_school # 删除整个变量
## 4. 改
# 无
## 5. 查
### 5.1 切片
a = tuple_master_school[1:]
b = tuple_master_school[:5]
c = tuple_master_school[:5:3]
### 5.2 直接访问
d = tuple_master_school[1]
### 5.3 查索引index
e = tuple_master_school.index("master")
e = tuple_master_school.index("master", 1, 100)  # 寻找范围缩小为子list
## 6. 其他
### 6.1 +
tuple_master_school = (1, 2, "master", "school")
tuple_master_school_tmp = (3, 4)
res = tuple_master_school + tuple_master_school_tmp

### 6.2 *
tuple_master_school = (1, "master", "school")
res = tuple_master_school * 2

### 6.3 max,min
tuple_master_school = ("1", "master", "school")
print(max(tuple_master_school))  # 元素要求可以比较，比如都为字符串或者都为整数

### 6.4 count

### 6.5 元组不可变的理解
tuple_master_school = ([1,2], "master", "school")
tuple_master_school[0][0] = 10 # 元素的地址没有改变即可，内部内容可以变化。这是因为list创建好了之后重新赋值地址不变

### 6.6 自动装包和拆包
def fun():
    return 1,2,3
a = fun() # 自动装包为一个元组
a,b,c = fun() # 可以理解为自动装包后拆包为对应的元素


print(1)