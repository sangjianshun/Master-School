# 线程间通信
import threading
import time
import variables  # 注意和from chapter11.variables import detail_url_list的区别，后者有时候会导致列表已经改变而不看见的情况
detail_url_list = variables.detail_url_list


# 线程间的通信方式：共享变量。共享变量可能会导致变量改变，导致不安全，应该加锁才是安全的。
def get_detail_html(detail_url_list):
    # 爬取文章详情页
    while True:
        if detail_url_list:
            url = detail_url_list.pop()
            print("get detail html started")
            time.sleep(2)
            print("get detail htm end")

def get_detail_url(detail_url_list):
    # 爬取文章列表页
    while True:
        print("get detail html started")
        time.sleep(2)
        for i in range(20):
            detail_url_list.append("thhp://projectsedu.com/{id}".format(id=i))
        print("get detail htm end")



if __name__ == '__main__':
    thread_detail_url = threading.Thread(target=get_detail_url, args = (detail_url_list,))
    for i in range(10):
        html_thread = threading.Thread(target = get_detail_html, args = (detail_url_list,))
        html_thread.start()
    # thread1 = threading.Thread(target=get_detail_html, args = ("",))
    # thread2 = threading.Thread(target=get_detail_url, args = ("",))
    # 当主线程退出的时候，子线程kill掉
    # thread1.setDaemon(True) # 守护线程，不需要等这个线程运行结束，即主线程运行结束就结束了。
    # thread2.setDaemon(True)
    start_time = time.time()
    # thread1.start()
    # thread2.start()
    #
    # thread1.join() # 需要等该线程运行结束。注意总时间是所有线程的最大值，不是和
    # thread2.join()
    print("last time: {}".format(time.time() - start_time))
