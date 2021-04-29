import time
from multiprocessing import Process, Queue, Pool, Manager, Pipe



# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
#
#
# if __name__ == '__main__':
#     queue = Queue(10) # 这个Queue和多线程不一样
#     my_producer = Process(target=producer, args=(queue,))
#     my_consumer = Process(target=consumer, args=(queue, ))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()


# # 共享全局变量不能适用于多进程编程，可以适用于多线程
# def producer(a):
#     a += 100
#     time.sleep(2)
#
# def consumer(a):
#     time.sleep(2)
#     print(a)
#
#
#
# if __name__ == '__main__':
#     a = 1
#     my_producer = Process(target=producer, args=(a,))
#     my_consumer = Process(target=consumer, args=(a, ))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()


# multiprocessing中的queue不能用于pool进程池,进程间的通信
# pool中的进程间通信需要使用manager中的queue

# 三个Queue
# from queue import Queue
# from multiprocessing import Queue
# from multiprocessing import Manager
# Manager().Queue()

# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
#
#
# if __name__ == '__main__':
#     # queue = Queue(10) # 这个Queue和多线程不一样
#     queue = Manager().Queue()
#     pool = Pool(2)
#
#     pool.apply_async(producer, args=(queue, ))
#     pool.apply_async(consumer, args=(queue, ))
#
#     pool.close()
#     pool.join()


# 通过pipe实现进程间通信
# pipe的性能高于queue，但是只适用于两个进程间的通信

# def producer(pipe):
#     pipe.send("test")
#
# def consumer(pipe):
#     data = pipe.recv()
#     print(data)
#
#
#
# if __name__ == '__main__':
#     # pipe只能适用于两个进程间的通信
#     receive_pipe, send_pipe = Pipe()
#
#     my_producer = Process(target=producer, args=(send_pipe,))
#     my_consumer = Process(target=consumer, args=(receive_pipe,))
#
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()


# 使用Manager().dict()进行进程间的通信
def add_data(p_dict, key, value):
    p_dict[key] = value

if __name__ == '__main__':

    progress_dict = Manager().dict()
    first_progress = Process(target=add_data, args = (progress_dict, "test1", 11))
    second_progress = Process(target=add_data, args = (progress_dict, "test2", 22))

    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()
    print(progress_dict)


