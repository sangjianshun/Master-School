import time
from concurrent import futures

# 线程池，为什么要线程池

# 当主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值

# 当一个线程完成的时候我们主线程能立即知道

# futures可以让多线程和多进程编码接口一致
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures import as_completed


def get_html(times):
    time.sleep(times)
    print(f"get page {times} success")

executor = ThreadPoolExecutor(max_workers=2)
# # 通过submit函数提交执行的函数到线程池中, submit是立即返回
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))
#
#
#
# print(task1.done())
# print(task2.cancel()) # 取消该任务，如果是在执行中或者执行完成，则会取消失败，返回False
# time.sleep(4)
# print(task1.done()) # done方法用于判定某个任务是否完成
#
# print(task1.result()) # result方法可以获取task的执行结果

urls = [3,2,4]
all_task = [executor.submit(get_html, (url)) for url in urls]
# wait(all_task, return_when="ALL_COMPLETED")
# print("test")

for future in as_completed(all_task):
    data = future.result()
    print(f"get {data} page")
#
# # 通过executor获取已经完成的task
for data in executor.map(get_html, urls):
    print(f"get {data} page") # map返回的结果顺序和传入的顺序一致