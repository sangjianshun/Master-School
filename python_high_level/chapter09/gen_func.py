# 生成器函数，函数里只要有yield关键字

def gen_func():
    yield 1  # 返回了一个生成器对象，是在python编译字节码时产生的对象。
    yield 2  # 注意和return的区别，这为惰性求值，延迟求值提供了可能。

def func():
    return 1


def fib1(index):
    if index <= 2:
        return 1
    else:
        return fib1(index - 1) + fib1(index - 2)

def fib2(index):
    res_list = []
    n,a,b = 0,0,1
    while n < index:
        res_list.append(b)
        a,b = b,a+b
        n +=1
    return res_list
def gen_fib(index):
    n,a,b = 0,0,1
    while n < index:
        yield b
        a,b = b,a+b
        n +=1

print(fib2(10))
for item in gen_fib(10):
    print(item)

if __name__ == '__main__':

    gen = gen_func()
    for item in gen:
        print(item)

    res = func()

    pass
