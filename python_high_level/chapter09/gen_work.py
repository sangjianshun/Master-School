# python中函数的工作原理
import inspect
frame = None
def foo():
    bar()

def bar():
    global frame
    frame = inspect.currentframe()
    pass

# python.exe  会用一个叫做 PyEval_EvaluFramEx(c函数)去执行foo函数，首先创建一个栈帧（stack frame）

# python一切皆对象，栈帧对象，字节码对象
# 当foo调用子函数bar，又会创建一个栈帧
# 所有的栈帧都是分配在堆内存上，这就决定了栈帧可以独立于调用者存在

import dis
print("##########")
print(dis.dis(foo))

# 5           0 LOAD_GLOBAL              0 (bar)
# 2 CALL_FUNCTION            0
# 4 POP_TOP
# 6 LOAD_CONST               0 (None)
# 8 RETURN_VALUE
# None
print("###########")
foo()
print(frame.f_code.co_name)
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)
print("#############")

def gen_func():
    yield 1
    name = "t1"
    yield 2
    age = 10
    return "t2"
gen = gen_func()
print(dis.dis(gen))
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

# 34           0 LOAD_CONST               1 (1)
# 2 YIELD_VALUE
# 4 POP_TOP
#
# 35           6 LOAD_CONST               2 ('t1')
# 8 STORE_FAST               0 (name)
#
# 36          10 LOAD_CONST               3 (2)
# 12 YIELD_VALUE
# 14 POP_TOP
#
# 37          16 LOAD_CONST               4 (10)
# 18 STORE_FAST               1 (age)
#
# 38          20 LOAD_CONST               5 ('t2')
# 22 RETURN_VALUE
# None
# -1
# {}
# 2
# {}
# 12
# {'name': 't1'}

a = [1,2,3]
for i in a:
    print(i)
from collections import UserList




