# 对于io操作来说，多线程和多进程性能差别不大
# 1.通过Thread类实例化
import threading
import time
# def get_detail_html(url):
#     print("get detail html started")
#     time.sleep(2)
#     print("get detail htm end")
#
# def get_detail_url(url):
#     print("get detail html started")
#     time.sleep(2)
#     print("get detail htm end")

# if __name__ == '__main__':
#     thread1 = threading.Thread(target=get_detail_html, args = ("",))
#     thread2 = threading.Thread(target=get_detail_url, args = ("",))
#     # 当主线程退出的时候，子线程kill掉
#     # thread1.setDaemon(True) # 守护线程，不需要等这个线程运行结束，即主线程运行结束就结束了。
#     # thread2.setDaemon(True)
#     start_time = time.time()
#     thread1.start()
#     thread2.start()
#
#     thread1.join() # 需要等该线程运行结束。注意总时间是所有线程的最大值，不是和
#     thread2.join()
#     print("last time: {}".format(time.time() - start_time))

#2.通过集成Thread来实现多线程

class GetDetailHtml(threading.Thread):
    def __init__(self,name):
        super().__init__(name = name)
    def run(self) -> None:
        print("get detail html started")
        time.sleep(2)
        print("get detail htm end")

class GetDetailUrl(threading.Thread):
    def __init__(self,name):
        super().__init__(name = name)
    def run(self) -> None:
        print("get detail html started")
        time.sleep(2)
        print("get detail htm end")

if __name__ == '__main__':
    thread1 = GetDetailHtml("GetDetailHtml")
    thread2 = GetDetailUrl("GetDetailUrl")
    # 当主线程退出的时候，子线程kill掉
    # thread1.setDaemon(True) # 守护线程，不需要等这个线程运行结束，即主线程运行结束就结束了。
    # thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()

    thread1.join() # 需要等该线程运行结束。注意总时间是所有线程的最大值，不是和
    thread2.join()
    print("last time: {}".format(time.time() - start_time))
