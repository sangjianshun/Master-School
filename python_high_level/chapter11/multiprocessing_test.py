# import os
# import time
# # fork只能用于linux/unix中
#
# # 运行fork，立马创建一个进程。进程之间数据完全隔离，
# # 子进程pid=0
# pid = os.fork()  # 子进程从这里开始再次运行
# print("test1")
# if pid == 0:
#     print(f"子进程 {os.getpid()}, 父进程是:{os.getppid()}")
# else:
#     print(f"我是父进程:{pid}")
#
# time.sleep(2) # 父进程退出，加上sleep可以等一下子进程



from concurrent.futures import ProcessPoolExecutor # 多进程编程,推荐使用这个
import multiprocessing # 比ProcessPoolExecutor更底层

# 多进程编程
import time
def get_html(n):
    time.sleep(n)
    print("sub progress success")
    return n

# class MyProgress(multiprocessing.process):
#     pass

if __name__ == '__main__':
    # progress = multiprocessing.Process(target=get_html, args = (2,))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print("main progress end")

    # 使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3,))
    #
    # # 等待所有任务完成
    # pool.close() # 不接收新的任务
    # pool.join()
    # print(result.get())


    # imap
    # for result in pool.imap(get_html, [1, 5, 3]): # 按照顺序
    #     print(f"{result} sleep success")

    for result in pool.imap_unordered(get_html, [1, 5, 3]): # 谁先执行完就先打印出来
        print(f"{result} sleep success")