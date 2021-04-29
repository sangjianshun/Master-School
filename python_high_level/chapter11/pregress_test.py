# 多进程编程
# 耗CPU的操作，用多进程编程，对于io操作来说，使用多线程编程，进程切换代价要高于线程。能使用多线程尽量使用多线程，

# 1、对于耗费cpu的操作，多进程优于多线程
import time


def fib(n):
    if n <=2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(2))

from concurrent.futures import ThreadPoolExecutor,as_completed # 多线程
from concurrent.futures import ProcessPoolExecutor # 多进程

# if __name__ == '__main__':
#
#     with ProcessPoolExecutor(3) as executor:
#         all_task = [executor.submit(fib, (num)) for num in range(25,35)]
#         start_time = time.time()
#         for future in as_completed(all_task):
#             data = future.result()
#             print("exe result:{}".format(data))
#         print(f"last time is :{time.time() - start_time}")



# 对于io操作来说，多线程优于多进程, 多线程可以开很多个，但是多进程不行，他更耗费内存
def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == '__main__':

    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2] * 30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result:{}".format(data))
        print(f"last time is :{time.time() - start_time}")