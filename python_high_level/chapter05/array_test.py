# array, deque

import array  # c语言的数组，存储是连续的存储空间，效率很高

my_array = array.array("i")  # int
my_array.append(1)
my_array.append("a") # TypeError: an integer is required (got type str)