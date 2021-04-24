from threading import Lock, RLock

total = 0
# Lock
# 1. 用锁会影响性能
# 2. 锁会有死锁的可能
# lock = Lock() # 影响并发性能

lock = RLock()
# RLock
# 在同一个线程里面，可以连续调用多次acquire，一定要注意acquire的次数要和release一致
# lock.acquire()
# lock.acquire()
# total +=1
# lock.release()
# lock.release()

def add():
    # 1. dosomething1
    # 2. io操作
    # 3. dosomething3
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        lock.acquire()
        total +=1
        lock.release()
        lock.release()

def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -=1
        lock.release()

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

def add1(a):
    a +=1
def desc(a):
    a -=1

"""
add1
1. load a
2. load 1
3. +
4. 赋值给a
"""
import dis

# print(dis.dis(add1))
# print(dis.dis(desc))


thread1.join()
thread2.join()
print(total)