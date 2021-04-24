b = [3, 4]

# list + list
a = [1, 2]
a = a + b # a=[1, 2, 3, 4]

# list += list
a = [1, 2]
a += b # a=[1, 2, 3, 4]

# list.extend(list)
a = [1, 2]
a.extend(b) # a=[1, 2, 3, 4]



b = (3,4)

# list + tuple 报错
# a = [1, 2]
# a = a + b # TypeError: can only concatenate list (not "tuple") to list

# list += tuple
a = [1, 2]
a += b # a=[1, 2, 3, 4]

# list.extend(tuple)
a = [1, 2]
a.extend(b) # a=[1, 2, 3, 4]